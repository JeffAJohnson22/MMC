import chromadb
from sentence_transformers import SentenceTransformer
from huggingface_hub import InferenceClient
import warnings
import logging
import glob

# Hide the warnings
warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)

chroma_client = chromadb.PersistentClient(path="./database")
model = SentenceTransformer("all-MiniLM-L6-v2")

# so new collections arent made every time
collection = chroma_client.get_or_create_collection(name="my_collection")

# Read all text files for this directory
txt_files = glob.glob("*.txt")
all_documents = []

for file in txt_files:
    with open(file, "r", encoding='ISO-8859-1') as f:
        text_content = f.read()
        # Split it into chunks
        chunks = [chunk.strip() for chunk in text_content.split('\n\n') if chunk.strip()]
        all_documents.extend(chunks)

# Calculate embeddings by calling model.encode()
embeddings = model.encode(all_documents)

# need upsert cause if its just add 
collection.upsert(
    documents=all_documents,
    embeddings=embeddings.tolist(),
    # can take as many as that are available
    ids=[f"id{i+1}" for i in range(len(all_documents))]
)

# Ask the Hugging Face API key from user
hf_api_key = input("Enter your Hugging Face API Key: ")

# Create the Hugging Face Inference Client
client = InferenceClient(model="meta-llama/Llama-3.1-8B-Instruct", token=hf_api_key)

# Loop fr the user to ask questions
while True:
    # Ask the user to enter their question
    user_question = input("\nEnter your question (or 'quit' to exit): ")
    
    # clause to end the loop
    if user_question.lower() == 'quit':
        print("Peace out")
        break
    
    # Query with custom embedding
    query_embedding = model.encode([user_question])
    
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
         # how many results to return
        n_results=3 
    )
    
    # Get the retrieved documents as context
    context = "\n".join(results['documents'][0])
    
    # Create messages for chat completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Answer the question using ONLY the provided context. If the answer is not in the context, say you do not know."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {user_question}"}
    ]
    
    # Get answer from Hugging Face model using chat completion
    output = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=messages,
        stream=False,
        max_tokens=1024
    )
    answer = output.choices[0].message.content
    
    # Display the answer
    print(f"\nAnswer: {answer}")


