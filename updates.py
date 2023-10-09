from pymongo import MongoClient

import time
url = "mongodb://localhost:27017"


client = MongoClient(url)

db = client["testme"]

doc = db["c1"]


doc.delete_many({})
r1 = doc.insert_many(
    [
        {"name": "nadika", "rollno": 12},
        {"name": "mahima", "rollno": 13},
        {"name": "nadika", "rollno": 33},
        {"name": "nadika", "rollno": 34},
        {"name": "nadika", "rollno": 1},
        {"name": "nadika", "rollno": 1},
        {"name": "nadika", "rollno": 1},
    ]
)

start=time.time()
doc.update_many({"rollno": 1}, {"$set": {"rollno": 34}})
end=time.time()
print(end-start)

start2=time.time()
for i in range(1, 8):
    doc.update_one({"rollno": 34}, {"$set": {"rollno": 34}})
end2=time.time()
print(end2-start2)




client.close()
