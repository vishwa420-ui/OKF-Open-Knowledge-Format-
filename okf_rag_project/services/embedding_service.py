import ollama

from config import EMBEDDING_MODEL, OLLAMA_HOST

client = ollama.Client(host=OLLAMA_HOST)


def create_embeddings(texts):

    if not texts:
        return []

    embeddings = []

    batch_size = 32

    for start in range(0, len(texts), batch_size):

        batch = texts[start:start + batch_size]

        response = client.embed(
            model=EMBEDDING_MODEL,
            input=batch
        )

        embeddings.extend(response.embeddings)

    return embeddings


def create_query_embedding(question):

    response = client.embed(
        model=EMBEDDING_MODEL,
        input=question
    )

    return response.embeddings[0]