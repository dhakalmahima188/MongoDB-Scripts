from pymongo import MongoClient
from pymongo import InsertOne, DeleteOne, UpdateOne


client = MongoClient('mongodb://localhost:27017')

db = client['homework']

collection = db['h1']

operations = [
    InsertOne({'name': 'mahima'}),
    InsertOne({'name': 'mahima'}),
    UpdateOne({'name': 'mahima'}, {'$set': {'age': 30}}),
    UpdateOne({'name': 'mahima'}, {'$set': {'age': 30}}),
    DeleteOne({'name': 'mahima'})
]

result = collection.bulk_write(operations)

print(result.inserted_count)
print(result.modified_count)
print(result.deleted_count)
