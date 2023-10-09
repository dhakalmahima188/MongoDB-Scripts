from pymongo import MongoClient

# Assuming you have a MongoDB connection
client = MongoClient("mongodb://localhost:27017")
database = client["test"]
collection = database["cp"]

# Get all the documents from the collection
documents = collection.find()


# Filter the documents based on fields ending with "_deletedSegment"
filtered_data = [doc for doc in documents if any(key.endswith("_cs") for key in doc.get("student", {}).keys())]

for doc in filtered_data:
    print(doc)

r1 = collection.update_many({}, {'$unset': {'*_cs': ""}})

r2 = collection.find()

for row in r2:
    print(row)
