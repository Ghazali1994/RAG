import chromadb

client = chromadb.PersistentClient(path="db")

collection = client.get_or_create_collection(
    name="tngov"
)

with open(
    "tn_data.txt",
    encoding="utf-8"
) as f:
    text = f.read()

collection.add(
    documents=[text],
    ids=["tn_home"]
)

print("Indexed")
