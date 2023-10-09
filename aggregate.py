from pymongo import MongoClient

url = "mongodb://localhost:27017/homework"

client = MongoClient(url)

db = client["homework"]

doc = db["h1"]
# print(doc.count_documents({'name':'mahima'}))
r1 = doc.insert_many(
    [
        {"name": "mahima", "mark": 20},
        {"name": "mahima", "mark": 30},
        {"name": "mahima", "mark": 40},
        {"name": "nadika", "mark": 40},
    ]
)

r2=doc.aggregate(
    [
        # {"$match": {"name": "mahima"}},
        {"$group": {"_id": "$name", "total": {"$sum": "$mark"}}},
       
    ]
)
for i in r2:
    print(i)

client.close()
