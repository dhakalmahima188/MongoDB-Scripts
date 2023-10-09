from pymongo import MongoClient, WriteConcern
import time

client = MongoClient('mongodb://localhost:27017')


db = client['test']

collection = db['h1']

start_time = time.time()
for i in range(1000):
    result = collection.insert_one({"name": "x"})

end_time = time.time()
print(collection.count_documents({}))
if result.acknowledged:
    print("Insert operation acknowledged.")
else:
    print("Insert operation not acknowledged.")

time_taken = end_time - start_time
print(f"Time taken: {time_taken} seconds")


#$ python3 timeoteacher.py
# 1000
# Insert operation acknowledged.
# Time taken: 0.3186025619506836 seconds