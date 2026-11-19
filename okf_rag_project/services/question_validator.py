from config import ALLOWED_TOPICS, REJECTION_MESSAGE

def validate_question(question):

    if not question or len(question.strip()) < 2:
        return False, "Please enter a valid question."

    allowed_keywords = {
        "python": [
            "python", "list", "tuple", "dictionary",
            "function", "loop", "class", "variable"
        ],
        "machine_learning": [
            "machine learning", "regression",
            "classification", "random forest",
            "decision tree", "model training"
        ],
        "deep_learning": [
            "deep learning", "neural network",
            "cnn", "rnn", "transformer"
        ],
        "rag": [
            "rag", "retrieval", "embedding",
            "vector database", "chromadb",
            "ollama", "knowledge base"
        ]
    }

    question = question.lower()

    for topic in ALLOWED_TOPICS:

        keywords = allowed_keywords.get(topic, [])

        if any(keyword in question for keyword in keywords):
            return True, None

    return False, REJECTION_MESSAGE