from sentence_transformers import SentenceTransformer
import chromadb

from ingest import load_documents, create_chunks

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = load_documents()
chunks = create_chunks(documents)

print(f"Loaded {len(chunks)} chunks")

client = chromadb.PersistentClient(path="../chroma_db")

collection = client.get_or_create_collection(
    name="uic_guide",
    metadata={"hnsw:space": "cosine"}
)

for i, chunk in enumerate(chunks):

    embedding = model.encode(chunk["text"]).tolist()

    collection.add(
        ids=[str(i)],
        embeddings=[embedding],
        documents=[chunk["text"]],
        metadatas=[{
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"]
        }]
    )

print("Embeddings stored successfully!")