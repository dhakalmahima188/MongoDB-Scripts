from pymongo import MongoClient

url = "mongodb://localhost:27017"
client = MongoClient(url)

db = client["test2"]
collection = db["test"]

collection.insert_one(
    [
        {
            "name": "mahima",
            "teacher": {},
            "student": {
                
                "mahima_cp": [{"ObjectId": "12345"}],
                "00511_cp": [
                    "123",
                    "24"
                    
                ],
            },
        },
    ]
)

documents = collection.find(
    {
        "$or": [
            {"student": {"$exists": True}},
            {"admin": {"$exists": True}},
            {"teacher": {"$exists": True}},
        ]
    }
)

update = {"$unset": {}}

for doc in documents:
    unset_fields = {}
    for i in ["student", "admin", "teacher"]:
        inner_dict = doc.get(i, {})
        for key in inner_dict:
            if key.endswith("_cp"):
                unset_fields[i + f".{key}"] = ""
    if unset_fields:
        update["$unset"] = unset_fields
        result = collection.update_one({"_id": doc["_id"]}, update)

r1 = collection.find()
for row in r1:
    print(row)

 