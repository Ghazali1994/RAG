import chromadb

client = chromadb.PersistentClient(path="db")

collection = client.get_collection("tngov")

query = input("Question: ")

results = collection.query(
    query_texts=[query],
    n_results=1
)

print(results["documents"][0][0][:1000])
