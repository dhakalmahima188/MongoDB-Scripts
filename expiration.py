from pymongo import MongoClient

url = "mongodb://localhost:27017/homework"

client = MongoClient(url)

db = client["hw"]
# db = client.get_database('hw')

doc = db["h1"]
# print(doc.count_documents({'name':'mahima'}))

doc.delete_many({})
r1 = doc.insert_many(
    [
        {"name": "mahima", "mark": 22},
        {"name": "mahima", "mark": 30},
        {"name": "mahima", "mark": 10},
        {"name": "mahima", "mark": 12},
        {"name": "mahima", "mark": 40},
    ]
)


#print(len(r1.inserted_ids))


# d1=doc.find({'name':{'$in':['mahima','nadika']}})
# for i in d1:
#     print(i)
# d2=doc.find({'mark':{'$all':[20,30]}})

# for i in d2:
#     print(i)

d1 = doc.find({"mark": {"$gt": 20, "$lt": 30}})
for i in d1:
    print(i)

doc.create_index('last_modified',expireAfterSeconds=2)
for i in doc.find():
    print(i)

# d2 = doc.find({"mark": {"$gt": 20}})
# d3 = doc.count_documents({"mark": {"$gt": 20}})
# print(d3)
# for i in d2:
#     print(i)

# # doc.update_one({"mark": 20}, {"$set": {"mark": 100}})
# doc.update_many({"mark": 20}, {"$set": {"mark": 100}})
client.close()
