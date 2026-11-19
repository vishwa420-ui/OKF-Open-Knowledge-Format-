# OKF + RAG Knowledge Assistant

A locally running, restricted Knowledge-Based AI Assistant built using **Ollama, Qwen, Nomic Embeddings, ChromaDB, FastAPI, and HTML/CSS/JavaScript**.

The system retrieves information from Markdown knowledge documents and generates answers using a local LLM. It is designed to answer questions based on the available knowledge base rather than act as an unrestricted general-purpose chatbot.

---

## 1. Project Overview

### Main Features

- Local AI model using Ollama.
- Qwen for answer generation.
- Nomic Embed Text for text embeddings.
- ChromaDB for vector storage and semantic retrieval.
- RAG pipeline for context-based answers.
- Markdown-based knowledge management.
- Configurable topic restrictions.
- Similarity-distance filtering.
- FastAPI backend.
- HTML, CSS, and JavaScript frontend.
- Source information returned with answers.
- No OpenAI API key or OpenAI API credits required for local inference.

## 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Ollama | Local LLM execution |
| Qwen 2.5 0.5B | Answer generation |
| Nomic Embed Text | Text embeddings |
| ChromaDB | Vector database |
| FastAPI | Backend API |
| HTML | Frontend structure |
| CSS | Frontend design |
| JavaScript | Frontend functionality |
| YAML | Knowledge metadata |

## 3. Project Folder Structure

```text
okf_rag_project/
│
├── main.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── knowledge/
│   ├── index.md
│   ├── python.md
│   ├── machine_learning.md
│   ├── deep_learning.md
│   └── rag.md
│
├── services/
│   ├── __init__.py
│   ├── okf_loader.py
│   ├── chunker.py
│   ├── embedding_service.py
│   ├── vector_store.py
│   ├── rag_service.py
│   └── question_validator.py
│
├── chroma_db/
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

## 4. System Architecture

```text
              USER
                |
                v
         FRONTEND (HTML/CSS/JS)
                |
                v
          FASTAPI BACKEND
                |
                v
       QUESTION VALIDATION
                |
                v
          QUERY EMBEDDING
                |
                v
          NOM​IC EMBEDDINGS
                |
                v
          CHROMADB SEARCH
                |
                v
        RELEVANT DOCUMENTS
                |
                v
          CONTEXT FILTER
                |
                v
           QWEN MODEL
                |
                v
        ANSWER + SOURCES
                |
                v
             USER
```

## 5. Prerequisites

Install the following:

1. Python 3.10 or later.
2. Ollama.
3. Visual Studio Code.
4. Git (optional).

### Install Ollama Models

Download and install Ollama from:

https://ollama.com/

Open CMD and execute:

```bash
ollama pull qwen2.5:0.5b
```

Download the embedding model:

```bash
ollama pull nomic-embed-text
```

Check installed models:

```bash
ollama list
```

## 6. Installation

Open CMD inside the project directory.

### Step 1: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 2: Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Start Ollama

Ensure Ollama is running locally.

Default API address:

```text
http://localhost:11434
```

## 7. Configuration

Edit `config.py` to customize the project.

```python
CHAT_MODEL = "qwen2.5:0.5b"

EMBEDDING_MODEL = "nomic-embed-text"

OLLAMA_HOST = "http://localhost:11434"

COLLECTION_NAME = "okf_knowledge_ollama_nomic_v1"

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 150

TOP_K = 4

MAX_DISTANCE = 0.35

ALLOWED_TOPICS = [
    "python",
    "machine_learning",
    "deep_learning",
    "rag"
]
```

### Configuration Parameters

| Parameter | Description |
|---|---|
| CHAT_MODEL | Local chat model |
| EMBEDDING_MODEL | Embedding model |
| OLLAMA_HOST | Ollama server address |
| CHUNK_SIZE | Maximum chunk character length |
| CHUNK_OVERLAP | Overlapping characters |
| TOP_K | Number of retrieved chunks |
| MAX_DISTANCE | Maximum accepted cosine distance |
| ALLOWED_TOPICS | Permitted topic categories |

A lower cosine distance generally indicates a more similar result. `MAX_DISTANCE` is an experimental setting and must be calibrated against your own knowledge documents and test questions.

## 8. Knowledge Base Management

Add your Markdown files inside the `knowledge/` folder.

Example: `knowledge/python.md`

```yaml
---
type: python
title: Python Programming
tags:
  - python
  - programming
status: stable
---
```

Write your knowledge below the YAML metadata.

Example:

```markdown
# Python Programming

Python is a high-level programming language.

## Variables

Variables store data in a program.

Example:

```python
name = "Vishwa"
age = 21

print(name)
print(age)
```
```

You can add more Markdown files whenever you need to expand the knowledge base.

## 9. Running the Application

### Step 1: Start Backend

Run:

```bash
uvicorn main:app --reload
```

Backend address:

```text
http://127.0.0.1:8000
```

### Step 2: Open API Documentation

Visit:

http://127.0.0.1:8000/docs

### Step 3: Ingest Knowledge

Send a POST request to:

```text
/ingest
```

This loads Markdown documents, splits the content into chunks, generates embeddings, and stores them in ChromaDB.

### Step 4: Start Frontend

Open the `frontend` folder in VS Code.

Run `index.html` using Live Server.

Default frontend address:

```text
http://127.0.0.1:5500
```

## 10. API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Check service status |
| POST | `/ingest` | Load knowledge documents |
| POST | `/query` | Ask a question |
| GET | `/stats` | View vector and model information |

### Example Query

POST:

```text
http://127.0.0.1:8000/query
```

Request:

```json
{
    "question": "What is Python?"
}
```

Example response shape:

```json
{
    "status": "success",
    "question": "What is Python?",
    "answer": "Answer generated from retrieved knowledge.",
    "sources": [],
    "grounded": true
}
```

The actual answer and source list depend on the documents retrieved.

## 11. Question Restriction

The application uses multiple controls:

1. Keyword-based question validation.
2. Semantic search using Nomic embeddings.
3. Similarity-distance filtering.
4. Context-restricted Qwen generation.

Example test questions:

| Question | Expected behavior |
|---|---|
| What is Python? | Answer if available in knowledge base |
| Explain machine learning | Answer if documented |
| What is RAG? | Answer if documented |
| Who is Virat Kohli? | Reject |
| Tell me a joke | Reject |
| What is today's weather? | Reject |

**Important:** These controls reduce unrelated answers but do not mathematically guarantee that every generated statement is supported by a source. The `grounded` field indicates that relevant documents passed retrieval filtering; it is not an independent factuality verification result.

## 12. Troubleshooting

### Ollama connection error

Check whether Ollama is running:

```bash
ollama list
```

### Model not found

Download the model:

```bash
ollama pull qwen2.5:0.5b
```

### Embedding model error

```bash
ollama pull nomic-embed-text
```

### ChromaDB is empty

Call:

```text
POST /ingest
```

### Frontend connection error

Check:

- FastAPI is running.
- Frontend is running through Live Server.
- API URL is `http://127.0.0.1:8000`.
- CORS allows the frontend's actual origin.

### Changed embedding model

Use a new ChromaDB collection name in `config.py` when changing embedding models. Do not mix vectors created by incompatible embedding models in the same collection.

## 13. Future Improvements

- Advanced semantic question classification.
- Better document-level and sentence-level evidence verification.
- Automatic knowledge document updates.
- User authentication.
- Conversation history.
- Multiple knowledge domains.
- Admin dashboard.
- Document upload support.
- Improved answer evaluation.
- More capable local LLM models.

## 14. License

This project is intended for educational, research, and development purposes.

---

**Project:** OKF + RAG Knowledge Assistant  
**Backend:** FastAPI  
**LLM:** Ollama Qwen 2.5 0.5B  
**Embeddings:** Nomic Embed Text  
**Vector Database:** ChromaDB  
**Frontend:** HTML, CSS, JavaScript
