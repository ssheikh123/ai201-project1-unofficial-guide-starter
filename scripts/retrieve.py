from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="../chroma_db")

collection = client.get_collection(
    name="uic_guide"
)

def retrieve(query, k=5):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results


if __name__ == "__main__":

    query = input("Question: ")

    results = retrieve(query)

    for i in range(len(results["documents"][0])):

        print("\n" + "=" * 60)

        print(
            f"Source: "
            f"{results['metadatas'][0][i]['source']}"
        )

        print(
            f"Distance: "
            f"{results['distances'][0][i]}"
        )

        print("-" * 60)

        print(results["documents"][0][i])