from pymongo import MongoClient

url = "mongodb://localhost:27017"

client = MongoClient(url)

db = client["test"]

doc = db["cpss"]

filtered_table={"$or": [
            {"student": {"$exists": True}},
            {"admin": {"$exists": True}},
            {"teacher": {"$exists": True}}
        ]}

doc2=doc.find( filtered_table)
match_ids=[]
for document in doc2:   
                student_table=document.get("student",{})
                admin_table=document.get("admin",{})
                teacher_table=document.get("teacher",{})

                total_table={"student":student_table,"admin":admin_table,"teacher":teacher_table}
               
                for table_name,table in total_table.items():
                        for field_name, field_value in table.items():
                          
                          if field_name.endswith("_cs"):
                                    match_ids.append(document["_id"])  #unset Use
        
                                    print(f"{field_name}:{field_value}")
                                   


for match_id in match_ids: 
    r2=doc.update_one({"_id": match_id},{"$unset": {f"student.{field_name}": ""}})
 

