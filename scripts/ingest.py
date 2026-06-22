import os
import re
from pathlib import Path

DATA_DIR = Path("../data/raw")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

def clean_text(text):
    text = text.replace("&", "&")
    text = text.replace(" ", " ")

    text = re.sub(r"\s+", " ", text)

    return text.strip()

def load_documents():
    documents = []

    for file in DATA_DIR.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        cleaned = clean_text(text)

        documents.append(
            {
                "source": file.name,
                "text": cleaned
            }
        )

    return documents

def chunk_text(text,
               chunk_size=CHUNK_SIZE,
               overlap=CHUNK_OVERLAP):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        if len(chunk.strip()) > 0:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

def create_chunks(documents):
    all_chunks = []

    for doc in documents:

        chunks = chunk_text(doc["text"])

        for idx, chunk in enumerate(chunks):

            all_chunks.append(
                {
                    "source": doc["source"],
                    "chunk_id": idx,
                    "text": chunk
                }
            )

    return all_chunks

if __name__ == "__main__":

    documents = load_documents()

    print(f"\nLoaded {len(documents)} documents\n")

    print("FIRST CLEANED DOCUMENT:")
    print("-" * 50)
    print(documents[0]["text"][:1000])

    for doc in documents:
        doc_chunks = chunk_text(doc["text"])
        print(f"{doc['source']}: {len(doc_chunks)} chunks")

    chunks = create_chunks(documents)

    print(f"\nTotal Chunks: {len(chunks)}")

    print("\nSAMPLE CHUNKS")
    print("=" * 50)

    for i, chunk in enumerate(chunks[:5]):

        print(f"\nChunk {i+1}")
        print(f"Source: {chunk['source']}")
        print("-" * 50)
        print(chunk["text"])