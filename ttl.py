from pymongo import MongoClient
from datetime import datetime

url = "mongodb://localhost:27017"
client = MongoClient(url)
db = client["homework"]
doc = db["h9"]

doc.delete_many({})

documents = [
    {"name": "mahima", "mark": 12, "last_modified": datetime.utcnow()},
    {"name": "nadika", "mark": 40, "last_modified": datetime.utcnow()},
]
doc.insert_many(documents)

doc.create_index('last_modified', expireAfterSeconds=2)

for i in doc.find():
    print(i)

client.close()
