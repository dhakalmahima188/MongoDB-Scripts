# MongoDB

### mac
``` 
brew tap mongodb/brew
brew install mongodb-community@6.0
brew services start mongodb-community@6.0
brew services stop mongodb-community@6.0

sudo apt-get install -y mongodb-org
```

### linux
``` sudo apt-get install gnupg curl
curl -fsSL https://pgp.mongodb.com/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor
sudo apt-get update
sudo apt-get install -y mongodb-org
```
### setup docker
##### script handle
```shell
FROM python:latest
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY script2.py /
CMD [ "python3", "script2.py" ]

```

#### check Ip adress of docker container
```shell
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mongo_docker
```
###### first pull
```shell
docker run hello-world
```

###### build
```shell
docker build -t test
```

##### run
```shell
docker run test
```

#### run
```shell
open --background -a Docker
```

------------------------

### setup docker for mongo
```shell
docker images
docker pull mongo:latest 
docker run -d -p 2717:27017 -v ~/MongoDB:/data/db --name mongo_docker mongo:latest
docker ps
docker exec -it mongo_docker bash
mongosh
```

#### change permissions
```shell
 db.createUser({ user: 'user', pwd: 'user', roles: [{ role: 'readWrite', db: 'testdb' }] })
```
#### start mongodb server

``` 
mongosh
```

#### view dbs

``` 

show dbs
```

#### create db

``` 
use testdb
```

#### view current db

``` 
db
```

#### delete

``` 
db.dropDatabase()
```

#### collections

``` 
show collections
db.createCollection('col1')
db.col1.drop()

```

#### insert rows

```shell
db.col1.insert({
    'name':'mahima',
    'roll':33
})

db.col1.insertMany([{
    'name':'mahima',
    'roll':33
},
{
    'name':'nadika',
    'roll':36
}])
```

#### show all collection rows
```shell
db.col1.find()
db.col1.find().pretty()
db.col1.find({'name':'mahima'})
```
#### update single collection row
It updates the first available collection that matches the filter.
```shell
db.col1.updateOne({name:'mahima'},{ $set :{roll: 34}})
```
#### update all collection row
It updates all available collections that matches the filter.

```shell
db.col1.updateMany({name:'mahima'},{ $set :{roll: 34,name: 'Manoj'}})

db.col1.find({'name':'mahima'})

```

#### delete all
```shell

delete_result = collection.delete_many({})
print('Deleted', delete_result.deleted_count, 'documents')
```

# Scripts
#### Pymongo
```
pip3 install pymongo
```
##### know port at which mongo is running
```shell
from pymongo import MongoClient

# Connection URL
url = 'mongodb://localhost'

# Create a MongoClient
client = MongoClient(url)
#port
port = client.port
```

##### connect to the database
```shell
from pymongo import MongoClient

# Connection URL
url = 'mongodb://localhost:27017'

# Create a MongoClient
client = MongoClient(url)

# Get the database
db = client['testdb']

# Get the collection
collection = db['col1']
print("Collection:", collection)

```

### CRUD
```shell
from pymongo import MongoClient

url = 'mongodb://localhost:27017'
client = MongoClient(url)

db = client['testdb2']


db.create_collection('col3')
doc = db['col3']


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
```


### Print all fields
```shell
r1=doc.find()
for row in r1:
    print(row)

```

#### Alter Fields in the table
```shell
r1 = doc.update_many({}, {'$unset': {'isd': ""}})
r2 = doc.find()
for row in r2:
    print(row)
```

#### Find character matching field-values only
```shell
r2 = doc.find({'name': {'$regex': '^na'}})
```


#### Get fieldname and values of a document
```shell
student_table = document["student"]
        for field_name, field_value in student_table.items():
            print(field_name, field_value)
```

#### Filter Fields that ends with a character or string
```shell
if field_name.endswith("_cs"):
                print(field_name, field_value)
                print(document["_id"])
```
#### Update the document if it matches the regx
```shell
doc.update_many(
                    {"_id": document["_id"]},
                    {"$unset": {f"teacherTable.{field_name}": ""}}
                 )
```

#### Deleting the field if  it ends with _cs
```shell
from pymongo import MongoClient
url = "mongodb://localhost:27017"
client = MongoClient(url)

db = client["test"]
doc = db["customerPreference"]

doc.delete_many({})

doc.insert_many([
    {
        "name": "mahima",
        "studentTable":{},
        "teacherTable": {            
            "mahima_cs": [{"ObjectId": "12345"}],
        }
    },
     {
        "name": "nadika",
        "studentTable":{},
        "teacherTable": {
            
            "nadika_cs": [{"ObjectId": "12345"}],
        }
    },
    {
        "name": "nadika",
        "studentTable":{},
        "teacherTable": {}  
             
}
    }]
)

r1=doc.find()
for row in r1:
    print(row)

for document in doc.find():
    #print(document)
    if "teacherTable" in document:
        student_table = document["teacherTable"]
       # print(student_table)
        for field_name, field_value in student_table.items():
            if field_name.endswith("_cs"):
              #  print(field_name, field_value)
                print(document["_id"])
                doc.update_many
                (
                    {"_id": document["_id"]},
                    {"$unset": {f"teacherTable.{field_name}": ""}}
                )
r1=doc.find()
for row in r1:
    print(row)


```