#import file function from pymongo
from pymongo import MongoClient
#refer to specific cluster
url = "mongodb+srv://admin:admin@cluster0.2pmbegp.mongodb.net/pytech"
#set function with cluster information
client = MongoClient(url)
#set database to pull from and insert into
db = client.pytech
#update specific document in specific collection within the database
result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Flintstone Jr."}})
#pull specified data from all documents within the specific collection
docs = db.students.distinct('student_id')
docs2 = db.students.distinct('first_name')
docs3 = db.students.distinct('last_name')
#display pulled data in pre-determined order
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for x,y,z in zip(docs,docs2,docs3):
    print(f"Student ID: {x}")
    print(f"First Name: {y}")
    print(f"Last Name: {z}")
#pull specified data from a specific document based a search within the specific collection
doc = db.students.find_one({"student_id": "1007"})
#display pulled data in pre-determined order
print("\n\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")
#enable the user to close the program with any key
again = input("\n\nEnd of program, press any key to exit...")
if again:
  quit()
