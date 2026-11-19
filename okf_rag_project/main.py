from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

import ollama

from config import OLLAMA_HOST, CHAT_MODEL, EMBEDDING_MODEL

from services.rag_service import (
    ingest_knowledge,
    ask_question
)

from services.vector_store import get_collection_count


app = FastAPI(
    title="OKF Restricted RAG API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


ollama_client = ollama.Client(host=OLLAMA_HOST)


class QueryRequest(BaseModel):

    question: str = Field(min_length=2)

    concept_type: str | None = None


@app.get("/")
def home():

    return {
        "message": "OKF RAG API is running"
    }


@app.get("/health")
def health():

    try:

        models = ollama_client.list()

        return {
            "status": "online",
            "models": [
                model.model for model in models.models
            ],
            "stored_vectors": get_collection_count()
        }

    except Exception as error:

        raise HTTPException(
            status_code=503,
            detail=str(error)
        )


@app.post("/ingest")
def ingest():

    try:

        result = ingest_knowledge()
        return {
            **result,
            "total_vectors": get_collection_count()
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.post("/query")
def query(request: QueryRequest):

    try:

        result = ask_question(
            request.question,
            request.concept_type
        )

        return {
            "status": "success",
            "question": request.question,
            "answer": result["answer"],
            "sources": result["sources"],
            "grounded": result["grounded"]
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.get("/stats")
def stats():

    return {
        "total_vectors": get_collection_count(),
        "chat_model": CHAT_MODEL,
        "embedding_model": EMBEDDING_MODEL
    }