import chromadb

from config import CHROMA_DIR, COLLECTION_NAME

client = chromadb.PersistentClient(
    path=str(CHROMA_DIR)
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"}
)


def replace_concept(concept_id, chunks, embeddings, metadatas, ids):

    existing = collection.get(
        where={"concept_id": concept_id}
    )

    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    if chunks:

        collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas
        )


def search_vectors(query_embedding, top_k=4, concept_type=None):

    count = collection.count()

    if count == 0:
        return []

    where = None

    if concept_type:
        where = {"type": concept_type}

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, count),
        where=where,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    output = []

    for i in range(len(results["ids"][0])):

        output.append({
            "content": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i]
        })

    return output


def get_collection_count():
    return collection.count()