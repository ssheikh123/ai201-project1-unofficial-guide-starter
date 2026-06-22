from pathlib import Path

CHUNK_SIZE = 100
OVERLAP = 20

raw_dir = Path("../data/raw")

documents = []

for file in raw_dir.glob("*.txt"):
    text = file.read_text(encoding="utf-8")

    documents.append({
        "source": file.name,
        "text": text.strip()
    })

print(f"Loaded {len(documents)} documents")

chunks = []

for doc in documents:
    text = doc["text"]

    start = 0

    while start < len(text):
        chunk = text[start:start + CHUNK_SIZE]

        if chunk.strip():
            chunks.append({
                "source": doc["source"],
                "text": chunk
            })

        start += CHUNK_SIZE - OVERLAP

print(f"Created {len(chunks)} chunks")

print("\n===== SAMPLE CHUNKS =====\n")

for i, chunk in enumerate(chunks[:5]):
    print(f"\nChunk {i+1}")
    print(f"Source: {chunk['source']}")
    print("-" * 50)
    print(chunk["text"][:400])