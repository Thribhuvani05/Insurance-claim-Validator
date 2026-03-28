import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_policy_chunks(path):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def create_vector_store(policy_path):
    chunks = load_policy_chunks(policy_path)
    embeddings = model.encode(chunks)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, chunks

def retrieve_clauses(query, index, chunks, top_k=3):
    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, top_k)
    return [chunks[i] for i in indices[0]]
