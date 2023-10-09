from pymongo import MongoClient

url = "mongodb://localhost:27017"

client = MongoClient(url)

db = client["test"]

doc = db["test_session2"]

doc.insert_one({
    "name": "mahima",
    "123_cp": [
        {"ObjectId": "12345"}
    ]
})

pipeline = [
    {
        "$project": {
            "arrayData": {
                "$objectToArray": "$$ROOT"
            }
        }
    },
    {
        "$match": {
            "arrayData.k": {"$regex": "cp$"}
        }
    }
]

result = list(doc.aggregate(pipeline))

for row in result:
    print(row)
