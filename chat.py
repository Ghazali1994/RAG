import chromadb
import requests

client = chromadb.PersistentClient(
    path="db"
)

collection = client.get_collection(
    "tngov"
)

question = input("Ask: ")

results = collection.query(
    query_texts=[question],
    n_results=1
)

context = results["documents"][0][0]

prompt = f"""
Answer using only this information.

Context:
{context}

Question:
{question}
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model":"gemma3:4b",
        "prompt":prompt,
        "stream":False
    }
)

print(
    response.json()["response"]
)
