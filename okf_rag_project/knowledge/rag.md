---
type: Concept
title: Retrieval Augmented Generation
tags:
  - rag
  - generative-ai
  - artificial-intelligence
  - llm
  - embeddings
  - vector-database
  - python
status: stable
---

# Retrieval Augmented Generation

## 1. Introduction to Retrieval Augmented Generation

Retrieval Augmented Generation (RAG) is an AI architecture that combines information retrieval techniques with Large Language Models (LLMs) to generate accurate and contextually relevant responses using external knowledge sources. Instead of depending entirely on the information learned during model training, RAG retrieves relevant information from external documents, databases, websites, or knowledge bases and provides that information to an LLM as additional context.

RAG is particularly useful when applications need to answer questions using private documents, organizational knowledge, technical manuals, research papers, company policies, or frequently updated information. It helps reduce unsupported answers, improves factual grounding, and allows developers to update the knowledge base without retraining the entire language model.

## 2. Why RAG Is Needed

Large Language Models are trained on large datasets, but they may not contain the latest information or private organizational knowledge. They can also generate hallucinations, which are responses that sound convincing but contain incorrect or unsupported information.

RAG addresses these limitations by retrieving relevant information from an external knowledge source before generating an answer. This allows the LLM to use specific, updated, and domain-related information when responding to user queries.

The main benefits of RAG include knowledge updating without model retraining, access to private documents, improved factual grounding, source-based answers, reduced dependence on model training knowledge, and better domain-specific question answering.

## 3. How RAG Works

RAG generally operates through two major pipelines: the ingestion pipeline and the query pipeline. The ingestion pipeline prepares documents and stores their embeddings in a vector database. The query pipeline converts user questions into embeddings, retrieves relevant document chunks, and supplies them to an LLM to generate a response.

### RAG Architecture

1. Document Loading: Import documents from PDFs, text files, Word documents, websites, or databases.
2. Text Extraction: Extract readable content from the source documents.
3. Text Cleaning: Remove unnecessary formatting, duplicate content, and irrelevant characters.
4. Text Chunking: Divide large documents into smaller text segments.
5. Embedding Generation: Convert text chunks into numerical vector representations.
6. Vector Storage: Store embeddings and associated metadata in a vector database.
7. Query Embedding: Convert the user's question into an embedding.
8. Similarity Search: Compare the query embedding with stored document embeddings.
9. Context Retrieval: Retrieve the most relevant document chunks.
10. Prompt Construction: Combine the user question with retrieved context.
11. LLM Generation: Send the prompt to a language model.
12. Response Generation: Return an answer grounded in the retrieved information.

## 4. RAG Architecture Components

A RAG system consists of several components that work together to retrieve external knowledge and generate meaningful answers.

**Document Loader:** A document loader reads information from different file formats and converts it into a common document representation.

**Text Splitter:** A text splitter divides large documents into smaller chunks to improve retrieval precision and fit context-window limits.

**Embedding Model:** An embedding model converts text into numerical vectors that represent semantic meaning.

**Vector Database:** A vector database stores embeddings and supports similarity-based retrieval of relevant information.

**Retriever:** A retriever searches the stored knowledge base and selects relevant document chunks based on a user query.

**Prompt Template:** A prompt template organizes the user question, retrieved context, and instructions into a structured input for the LLM.

**Large Language Model:** An LLM processes the retrieved context and generates a natural-language answer.

## 5. Ingestion Pipeline

The ingestion pipeline is responsible for preparing knowledge sources before users start asking questions. It loads documents, extracts text, cleans the content, splits it into chunks, generates embeddings, and stores them in a vector database.

The ingestion pipeline is generally executed when documents are initially added or when the knowledge base needs to be updated. Separating ingestion from querying improves performance because documents do not need to be processed again for every user question.

### Document Loading

Document loading is the first stage of the ingestion pipeline. It imports information from different sources, such as PDF files, Word documents, Markdown files, text files, HTML pages, and databases.

Python libraries such as PyPDF, python-docx, BeautifulSoup, and LangChain document loaders can be used to extract information from different sources.

### Text Extraction

Text extraction converts document contents into machine-readable text. For example, a PDF loader extracts paragraphs, headings, and other readable content from PDF pages.

Scanned documents may require Optical Character Recognition (OCR) because their content is stored as images instead of directly extractable text.

### Text Cleaning

Text cleaning removes unwanted characters, unnecessary spaces, duplicated content, and formatting problems from extracted text. Clean text helps improve the quality of embeddings and retrieval results.

### Text Chunking

Text chunking is the process of dividing large documents into smaller text segments called chunks. Embedding an entire large document as a single vector can reduce retrieval precision because multiple topics may be represented in the same embedding.

Chunking makes it possible to retrieve specific sections that are relevant to a user's question.

Common chunking techniques include:

- Fixed-Size Chunking: Divides text into chunks based on a predefined character or token length.
- Recursive Character Chunking: Splits text using a hierarchy of separators such as paragraphs, lines, and sentences.
- Sentence-Based Chunking: Divides text according to sentence boundaries.
- Semantic Chunking: Groups text according to semantic relationships and changes in meaning.
- Structure-Aware Chunking: Uses document structures such as headings, sections, tables, and paragraphs.

### Chunk Size and Overlap

Chunk size determines how much text is stored in each chunk. Smaller chunks can provide more precise retrieval, while larger chunks can preserve more surrounding context.

Chunk overlap is the amount of text shared between consecutive chunks. It helps prevent important information from being lost when a sentence or concept crosses a chunk boundary.

For example, a document can be divided into 500-token chunks with 100-token overlap. These are example settings rather than universal optimal values.

## 6. Embeddings

Embeddings are numerical representations of text, images, or other data that capture meaningful features and relationships. In RAG systems, text embedding models convert document chunks and user queries into numerical vectors so that semantically related content can be retrieved even when the exact words are different.

For example, the questions "How does machine learning work?" and "Explain the working process of ML" may have similar semantic embeddings even though they use different words.

An embedding model maps text into a vector space where related meanings are represented by nearby vectors according to the model's learned representation.

### How Embeddings Work

1. Input text is provided to an embedding model.
2. The model processes the text using its learned neural network representations.
3. The model generates a numerical vector.
4. The vector represents semantic and contextual information.
5. Similar texts can be compared using vector similarity calculations.

### Embedding Example

```python
from openai import OpenAI

client = OpenAI()

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="What is Machine Learning?"
)

embedding = response.data[0].embedding

print("Vector Dimensions:", len(embedding))
print("Embedding:", embedding[:10])
```

### Types of Embedding Models

Embedding models are available for different tasks and modalities. Some models specialize in text embeddings, while others support multilingual content, images, or multimodal representations.

Common embedding model examples include:

- OpenAI text-embedding-3-small.
- OpenAI text-embedding-3-large.
- BAAI BGE models.
- Sentence Transformers.
- Google embedding models.
- E5 embedding models.
- Cohere Embed models.

### Embedding Dimensions

Embedding dimensions represent the number of numerical values in an embedding vector. For example, an embedding model may generate a vector containing 384, 768, 1536, or more dimensions.

The dimensionality depends on the embedding model and its configuration. The same embedding model and compatible dimensions must be used for document embeddings and query embeddings in a vector search system.

## 7. Vector Databases

A vector database is a specialized database designed to store, index, and retrieve numerical vectors efficiently. RAG systems use vector databases to store document embeddings and identify relevant information through similarity search.

Unlike traditional databases that primarily perform exact matching, vector databases can retrieve semantically related information based on numerical similarity.

Common vector databases and vector search technologies include:

- ChromaDB.
- FAISS.
- Pinecone.
- Weaviate.
- Qdrant.
- Milvus.
- PostgreSQL with pgvector.

### ChromaDB

ChromaDB is an open-source vector database designed for storing and retrieving embeddings. It supports document storage, metadata management, vector similarity search, and persistent storage.

ChromaDB can be integrated with embedding models and LLMs to build local or cloud-based RAG applications.

### ChromaDB Example

```python
import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="knowledge_base"
)

collection.add(
    ids=["1", "2"],
    documents=[
        "Python is a programming language.",
        "Machine Learning is a branch of AI."
    ],
    metadatas=[
        {"source": "python.md"},
        {"source": "ml.md"}
    ]
)

results = collection.query(
    query_texts=["What is Machine Learning?"],
    n_results=2
)

print(results["documents"])
```

ChromaDB can automatically generate embeddings when a compatible embedding function is configured. For production applications, configure and explicitly manage the embedding model so that document and query embeddings remain compatible.

## 8. Similarity Search

Similarity search is a retrieval technique used to identify document embeddings that are closest to a query embedding. The system calculates the similarity or distance between vectors and returns the most relevant results.

RAG systems commonly use cosine similarity, Euclidean distance, and dot product for vector comparison.

### Cosine Similarity

Cosine similarity measures the angle between two vectors. It is commonly used in text retrieval because it measures directional similarity rather than directly measuring vector magnitude.

The mathematical formula is:

Cosine Similarity = (A · B) / (||A|| × ||B||)

Here, A and B represent two embedding vectors, the dot product measures their alignment, and the vector magnitudes are used for normalization.

### Euclidean Distance

Euclidean distance measures the straight-line distance between two vectors in multidimensional space. Smaller distances indicate closer vectors.

### Dot Product

The dot product calculates the sum of the products of corresponding vector elements. It can be used as a similarity measure, particularly when embedding vectors are normalized or when the embedding model is trained for dot-product retrieval.

The appropriate similarity metric depends on the embedding model and vector database configuration.

## 9. Retrieval Techniques

Retrieval is the process of identifying relevant information from a knowledge base based on a user query. A good retrieval system should return relevant, accurate, and sufficiently informative document chunks.

### Dense Retrieval

Dense retrieval uses embedding vectors to find semantically similar documents. It can retrieve relevant information even when the query and document use different words.

### Sparse Retrieval

Sparse retrieval uses keyword-based representations to identify documents containing important query terms. BM25 is a commonly used sparse retrieval algorithm.

### Hybrid Search

Hybrid search combines dense vector retrieval with sparse keyword retrieval. It helps capture both semantic relationships and exact keyword matches.

For example, a query containing a specific product ID or technical error code may benefit from keyword retrieval, while a conceptual question may benefit from semantic retrieval.

### Top-K Retrieval

Top-K retrieval selects the K most relevant document chunks based on the retrieval score.

For example, if K is set to 5, the retriever returns the five highest-ranked results according to its search method.

### Metadata Filtering

Metadata filtering narrows retrieval results using additional document information such as source, category, author, date, department, or document type.

It is useful when an application needs to retrieve information from a specific document category or organization.

## 10. Reranking

Reranking is an additional retrieval stage that reorders initially retrieved document chunks according to their relevance to the user query.

A typical RAG system first retrieves a larger set of candidate documents using an embedding model and then applies a reranking model to identify the most relevant chunks.

Cross-encoder models are commonly used for reranking because they evaluate the query and each candidate document together rather than comparing independently generated embeddings.

Reranking can improve retrieval precision, particularly when the initial vector search returns several semantically similar but not equally useful documents.

## 11. Context Retrieval

Context retrieval selects the most relevant information from the retrieved document chunks and prepares it for the LLM. The retrieved content should contain enough information to answer the user's question without introducing unnecessary or unrelated material.

The retrieval system can also attach metadata such as document names, page numbers, source identifiers, and section titles to support traceability and source citations.

The quality of the retrieved context has a direct impact on the quality of the generated answer.

## 12. Prompt Engineering in RAG

Prompt engineering is the process of designing instructions that guide an LLM to generate appropriate responses. In RAG systems, prompts typically contain retrieved context, user questions, response instructions, and restrictions against unsupported claims.

A good RAG prompt should instruct the LLM to use the retrieved context as its primary source of information and clearly state when the answer is unavailable in the supplied documents.

### RAG Prompt Example

```text
You are a helpful AI assistant.

Answer the question using only the
provided context.

If the answer is not available in
the context, say that you do not
have enough information.

Context:
{retrieved_context}

Question:
{user_question}

Answer:
```

## 13. LLM Integration

A Large Language Model is responsible for generating the final response using the retrieved context and the user's question. The LLM receives a structured prompt and produces a natural-language answer.

Common LLM providers and model families used in RAG applications include OpenAI GPT models, Google Gemini, Anthropic Claude, Meta Llama, and other compatible open-source models.

The LLM can be accessed through an API or deployed locally, depending on application requirements, privacy constraints, available hardware, and cost considerations.

### OpenAI LLM Example

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "Answer using the provided context."
        },
        {
            "role": "user",
            "content": """
            Context:
            Machine Learning is a branch of AI.

            Question:
            What is Machine Learning?
            """
        }
    ]
)

print(response.choices[0].message.content)
```

## 14. Ingestion Pipeline vs Query Pipeline

A RAG application should generally separate document ingestion and user querying into independent pipelines.

**Ingestion Pipeline:** Responsible for loading documents, extracting text, cleaning content, generating chunks, creating embeddings, and storing vectors and metadata in the vector database. It runs when new documents are added or existing documents are updated.

**Query Pipeline:** Responsible for accepting user questions, generating query embeddings, retrieving relevant chunks, optionally reranking the results, constructing the prompt, calling the LLM, and returning the final answer.

Separating these pipelines improves modularity, performance, maintainability, and scalability.

## 15. Advanced RAG Techniques

Advanced RAG techniques improve retrieval quality, contextual understanding, and answer generation beyond a basic vector search implementation.

**Query Transformation:** Rewrites or modifies a user question to improve retrieval quality.

**Query Expansion:** Generates additional related search terms or alternative questions to retrieve more relevant documents.

**Multi-Query Retrieval:** Creates multiple variations of a user query and retrieves information using each variation.

**Parent-Child Retrieval:** Retrieves small chunks for precise matching while preserving their connection to larger parent sections for additional context.

**Sentence Window Retrieval:** Retrieves relevant sentences and expands the surrounding context to provide a more complete understanding.

**Contextual Compression:** Removes irrelevant information from retrieved documents before passing them to the LLM.

**Self-RAG:** Uses reflection and retrieval-related decisions to improve the relevance and reliability of generated answers.

**Corrective RAG (CRAG):** Evaluates retrieval quality and can use additional retrieval strategies when the retrieved information is insufficient.

**Graph RAG:** Uses relationships between entities and concepts represented in a knowledge graph to support more complex information retrieval.

**Agentic RAG:** Uses an AI agent to decide when and how to retrieve information, select tools, perform additional searches, and refine answers.

## 16. RAG Evaluation

RAG evaluation measures how effectively the system retrieves relevant information and generates accurate answers. Evaluating only the final answer is insufficient because poor responses may originate from either retrieval problems or generation problems.

### Retrieval Evaluation

**Precision@K:** Measures how many of the retrieved top-K results are relevant.

**Recall@K:** Measures how many of all relevant documents are retrieved within the top-K results.

**Mean Reciprocal Rank (MRR):** Measures how highly the first relevant search result appears in the ranked retrieval list.

**Normalized Discounted Cumulative Gain (NDCG):** Measures ranking quality while considering the relevance and position of retrieved results.

### Generation Evaluation

**Faithfulness:** Measures whether the generated answer is supported by the retrieved context.

**Answer Relevance:** Measures whether the generated answer directly addresses the user's question.

**Answer Correctness:** Measures whether the answer is factually correct compared with a reference answer.

**Context Relevance:** Measures whether the retrieved context is relevant to the user query.

Popular RAG evaluation tools include Ragas, DeepEval, TruLens, and custom evaluation frameworks.

## 17. RAG Hallucination and Limitations

RAG can reduce hallucinations by grounding LLM responses in retrieved information, but it does not completely eliminate hallucinations.

Incorrect document extraction, poor chunking, weak embeddings, irrelevant retrieval results, missing knowledge, misleading source documents, and poorly designed prompts can all affect answer quality.

A reliable RAG system should evaluate retrieval results, maintain trustworthy knowledge sources, provide source references, handle insufficient context, and monitor generated responses.

## 18. RAG Security

Security is important when building RAG applications that process confidential documents or private organizational knowledge.

Common security concerns include unauthorized document access, sensitive information exposure, prompt injection, malicious document content, insecure APIs, and improper metadata filtering.

RAG applications should implement authentication, authorization, access-controlled retrieval, input validation, secure API key management, document-level permissions, and appropriate logging policies.

Retrieved documents must be treated as untrusted data rather than executable instructions.

## 19. RAG Using Python Libraries

Python provides several libraries and frameworks for implementing RAG systems.

**OpenAI:** Provides embedding generation and LLM APIs.

**ChromaDB:** Provides vector storage, indexing, and similarity search.

**LangChain:** Provides components for document loading, text splitting, retrieval, prompt construction, and LLM integration.

**LlamaIndex:** Provides data ingestion, indexing, retrieval, and knowledge-based LLM application components.

**Sentence Transformers:** Provides pretrained embedding and reranking models.

**Hugging Face Transformers:** Provides access to pretrained language models and related NLP components.

**PyPDF:** Extracts text from PDF documents.

**FastAPI:** Provides API endpoints for exposing RAG functionality.

**Ragas:** Provides evaluation methods for RAG applications.

## 20. Complete RAG System Architecture

A production-oriented RAG system can be organized into separate components to simplify development and maintenance.

### Backend Architecture

- `main.py`: Application entry point.
- `ingestion.py`: Handles document ingestion.
- `loader.py`: Loads documents from different sources.
- `chunker.py`: Splits documents into smaller chunks.
- `embeddings.py`: Generates document and query embeddings.
- `vector_store.py`: Manages ChromaDB collections.
- `retriever.py`: Performs similarity search and retrieval.
- `reranker.py`: Reorders retrieved chunks when required.
- `prompt.py`: Manages prompt templates.
- `llm.py`: Integrates the language model.
- `rag_pipeline.py`: Coordinates the complete query pipeline.
- `api.py`: Exposes RAG functionality through FastAPI.
- `config.py`: Stores application configuration.

### RAG Data Flow

Documents → Loader → Text Extraction → Cleaning → Chunking → Embeddings → ChromaDB.

User Query → Query Embedding → Retriever → Reranker → Context → Prompt Template → LLM → Final Answer.

## 21. RAG API Development

FastAPI can be used to expose RAG functionality through REST APIs. A backend API can provide endpoints for uploading documents, triggering ingestion, querying the knowledge base, and retrieving source information.

Common API endpoints include:

**POST /ingest:** Uploads or processes documents and stores their embeddings.

**POST /query:** Accepts a question and returns a generated answer with relevant sources.

**GET /health:** Checks whether the backend application is running.

**GET /documents:** Retrieves document information from the knowledge base.

FastAPI supports request validation, asynchronous programming, dependency injection, and automatic API documentation.

## 22. RAG vs Fine-Tuning

RAG and Fine-Tuning are two different approaches for improving the behavior of Large Language Models.

RAG provides external knowledge to an LLM at inference time by retrieving relevant documents and adding them to the prompt. It is suitable when an application needs frequently updated information, private documents, or source-based answers.

Fine-Tuning modifies a model's learned parameters using additional training data. It is useful for adapting a model's behavior, response format, task performance, or domain-specific patterns.

RAG generally does not require retraining the LLM whenever documents change, whereas fine-tuning requires an additional training process when the model needs to learn new patterns.

## 23. RAG vs Traditional Search

Traditional search primarily identifies documents using keyword matching, metadata, or ranking algorithms. RAG goes further by retrieving relevant content and supplying it to an LLM to generate a natural-language response.

Traditional search generally returns documents or links, whereas RAG can synthesize information from multiple retrieved sources into a single contextual answer.

Hybrid RAG systems can combine keyword search, vector search, and language generation to provide more comprehensive question-answering capabilities.

## 24. Applications of RAG

RAG is used in applications that require intelligent access to external or private knowledge sources.

**Enterprise Knowledge Assistant:** Answers employee questions using internal company documents and policies.

**Healthcare Knowledge Assistant:** Retrieves information from medical references and authorized clinical documents to support information access.

**Legal Document Assistant:** Retrieves relevant sections from legal documents, contracts, and regulations.

**Educational Assistant:** Answers student questions using textbooks, notes, and educational materials.

**Customer Support Assistant:** Provides answers using product manuals, FAQs, and support documentation.

**Research Assistant:** Retrieves relevant information from scientific papers and research documents.

**Technical Documentation Assistant:** Answers programming and engineering questions using technical manuals and documentation.

**Personal AI Assistant:** Retrieves information from a user's private notes, files, and knowledge base.

## 25. RAG Production Optimization

Production RAG applications must be optimized for speed, cost, reliability, and retrieval quality.

Important optimization techniques include caching frequently requested results, selecting appropriate embedding models, optimizing chunk sizes, using efficient vector indexes, limiting unnecessary context, reranking candidate results, implementing asynchronous API calls, and monitoring token usage.

Additional techniques include batching embedding requests, incremental document ingestion, duplicate detection, retry mechanisms, rate-limit handling, request timeouts, and background processing for large ingestion jobs.

## 26. Important RAG Engineering Concepts

Developers building production RAG applications should understand several backend and AI engineering concepts.

**Routing:** Directs incoming requests to the appropriate retriever, knowledge base, model, or processing pipeline.

**Rate Limiting:** Restricts the number of API requests allowed within a specific time period to prevent abuse and control costs.

**Caching:** Stores frequently used responses, embeddings, or retrieval results to reduce repeated computation.

**Asynchronous Processing:** Allows applications to perform operations without blocking the main execution flow.

**Batch Processing:** Processes multiple documents or embedding requests together to improve efficiency.

**Retry Mechanism:** Repeats failed operations according to predefined rules.

**Timeout Handling:** Limits how long an application waits for an external service or operation.

**Logging:** Records application events, errors, requests, and execution details for monitoring and debugging.

**Authentication:** Verifies the identity of users accessing the RAG application.

**Authorization:** Controls which documents and resources authenticated users are permitted to access.

**Observability:** Helps developers monitor latency, failures, retrieval quality, token usage, and application performance.

## 27. Learning Roadmap for RAG Development

A structured learning path helps developers progress from basic document retrieval to production-grade RAG systems.

1. Python Programming Fundamentals.
2. API Development using FastAPI.
3. LLM Fundamentals.
4. Prompt Engineering.
5. Tokenization and Context Windows.
6. Embeddings and Semantic Search.
7. Vector Databases.
8. Document Loading and Text Extraction.
9. Text Chunking Strategies.
10. Similarity Search and Retrieval.
11. ChromaDB Integration.
12. OpenAI API Integration.
13. Hybrid Search and Reranking.
14. Advanced RAG Techniques.
15. RAG Evaluation.
16. RAG Security.
17. API Deployment and Optimization.
18. Production RAG and Monitoring.
19. Agentic RAG.

## 28. Conclusion

Retrieval Augmented Generation is an important architecture in modern Generative AI applications. It combines information retrieval, embedding models, vector databases, and Large Language Models to generate context-aware answers using external knowledge sources.

Understanding document ingestion, text chunking, embedding generation, vector storage, similarity search, retrieval, prompt engineering, and LLM integration is essential for building effective RAG systems.

Technologies such as OpenAI, ChromaDB, FastAPI, LangChain, LlamaIndex, and Ragas provide the components required to develop, evaluate, and deploy practical RAG applications.

RAG provides an important foundation for building enterprise AI assistants, knowledge management systems, intelligent document processing applications, and advanced Agentic AI systems.