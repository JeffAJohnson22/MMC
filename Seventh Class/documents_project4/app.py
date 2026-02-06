import chromadb
from sentence_transformers import SentenceTransformer

chroma_client = chromadb.PersistentClient(path="./database")

# Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
collection = chroma_client.get_or_create_collection(name="my_collection")

# The text chunks to encode
documents = [
    "This is a document about pineapple",
    "This is a document about oranges"
]

# Calculate embeddings by calling model.encode()
embeddings = model.encode(documents)
print(f"Embeddings shape: {embeddings.shape}")

# switch `add` to `upsert` to avoid adding the same documents every time
collection.upsert(
    documents=documents,
    embeddings=embeddings.tolist(),
    ids=["id1", "id2"]
)

# Query with custom embedding
query_text = "This is a query document about bananas"
query_embedding = model.encode([query_text])

results = collection.query(
    query_embeddings=query_embedding.tolist(),
    n_results=2 # how many results to return
)

print(results)
