from pymongo import MongoClient

url = "mongodb://localhost:27017"

client = MongoClient(url)

db = client["test"]

doc = db["test_session2"]

doc.insert_one({
    "name": "nadika",
    "0041_cs": [
        {"ObjectId": "ab9655556"}
    ],
   
})

r2 = doc.find({'name': {'$regex': '^na'}})

for row in r2:
    print(row)
