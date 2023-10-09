from pymongo import MongoClient

url = 'mongodb://localhost:27017'
# url = '172.0.0.1://localhost:27017'

client = MongoClient(url)

db = client['testdb2']
print('hello world')

db.create_collection('col887')
doc = db['col887']


doc.delete_many({})
r1=doc.insert_many([{'name':'nadika','rollno':1},{'name':'nabin','rollno':2}])
r2=doc.insert_one({'name':'mahima','rollno':33})
r3=doc.update_many({'name':'nabin'},{'$set':{'rollno':40}})
r4=doc.update_one({'rollno':1},{'$set':{'rollno':34}})

print(r1.inserted_ids)
print(r2.inserted_id)
print(r3.modified_count)
print(r4.modified_count)


client.close()