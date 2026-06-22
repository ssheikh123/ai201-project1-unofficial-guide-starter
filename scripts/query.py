from sentence_transformers import SentenceTransformer
import chromadb
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# ---- LLM ----
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---- embedding model ----
model = SentenceTransformer("all-MiniLM-L6-v2")

# ---- vector DB ----
chroma_client = chromadb.PersistentClient(path="../chroma_db")
collection = chroma_client.get_collection(name="uic_guide")


def retrieve(query, k=5):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results


def build_context(results):
    chunks = results["documents"][0]
    metas = results["metadatas"][0]

    context = ""

    sources = []

    for i in range(len(chunks)):
        source = metas[i]["source"]
        text = chunks[i]

        context += f"\n\nSOURCE: {source}\n{text}"
        sources.append(source)

    return context, list(set(sources))


def ask(question):
    results = retrieve(question)

    context, sources = build_context(results)

    prompt = f"""
You are a helpful assistant for answering questions about UIC Computer Science.

RULES:
- Use ONLY the provided context.
- If the answer is not in the context, say: "I don't have enough information in the provided documents."
- Do NOT use outside knowledge.
- Always stay grounded.

CONTEXT:
{context}

QUESTION:
{question}

Answer clearly and concisely.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You only answer using provided context."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    answer = completion.choices[0].message.content

    return {
        "answer": answer,
        "sources": sources
    }