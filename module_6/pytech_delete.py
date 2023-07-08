#import file function from pymongo
from pymongo import MongoClient
#refer to specific cluster
url = "mongodb+srv://admin:admin@cluster0.2pmbegp.mongodb.net/pytech"
#set function with cluster information
client = MongoClient(url)
#set database to pull from and insert into
db = client.pytech
#pull specified data from all documents within the specific collection
docs = db.students.distinct('student_id')
docs2 = db.students.distinct('first_name')
docs3 = db.students.distinct('last_name')
#display pulled data in pre-determined order
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for x,y,z in zip(docs,docs2,docs3):
    print(f"Student ID: {x}")
    print(f"First Name: {y}")
    print(f"Last Name: {z}\n")
#add new test document and data to the specific collection
barney = {
    "first_name": "Barney",
    "last_name": "Rubble",
    "student_id": "1010"
}
barney_student_id = db.students.insert_one(barney).inserted_id
#display inserted data via pre-determined method
print("\n-- Insert Statements --")
print(f"Inserted student record into the students collection with document_id {barney_student_id}")
#pull specified data from a specific document based a search within the specific collection
doc = db.students.find_one({"student_id": "1010"})
#display 2nd set of pulled data in pre-determined order
print("\n\n-- DISPLAYING STUDENT TEST DOC --")
print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")
#delete unwanted test data
delete = db.students.delete_one({"student_id": "1010"})
#pull specified data from all documents within the specific collection again
docs4 = db.students.distinct('student_id')
docs5 = db.students.distinct('first_name')
docs6 = db.students.distinct('last_name')
#display 3rd set of pulled data in pre-determined order
print("\n\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for x,y,z in zip(docs4,docs5,docs6):
    print(f"Student ID: {x}")
    print(f"First Name: {y}")
    print(f"Last Name: {z}\n")
#enable the user to close the program with any key
again = input("\nEnd of program, press any key to exit...")
if again:
  quit()
