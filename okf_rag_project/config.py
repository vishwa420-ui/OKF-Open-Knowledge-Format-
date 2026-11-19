from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

KNOWLEDGE_DIR = BASE_DIR / "knowledge"
CHROMA_DIR = BASE_DIR / "chroma_db"

# Change these models whenever required
CHAT_MODEL = "qwen2.5:0.5b"
EMBEDDING_MODEL = "nomic-embed-text"

OLLAMA_HOST = "http://localhost:11434"

# ChromaDB
COLLECTION_NAME = "okf_knowledge_ollama_nomic_v1"

# Chunk settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

# Retrieval settings
TOP_K = 4
MAX_DISTANCE = 0.35

# Change these to control permitted topics
ALLOWED_TOPICS = [
    "python",
    "machine_learning",
    "deep_learning",
    "rag"
]

# Rejection message
REJECTION_MESSAGE = (
    "I cannot answer this question because "
    "it is outside my knowledge base."
)