from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["h1"]

collection = db["book"]

# r1 = collection.insert_many(
#     [{"name": "python is a program"}, {"name": "mongoengine mahima"}]
# )
# print(r1.acknowledged)

result = collection.find({"$text": {"$search": "mahima"}})

# for document in result:
#     print(document)

result = collection.find({"or": [{"name": "python"}, {"name": "mongoengine"}]})


# for document in result:
#     print(document)

collection.create_index('last_modified',expireAfterSeconds=2)
for i in collection.find():
    print(i)
