from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.2pmbegp.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
docs = db.students.distinct('student_id')
docs2 = db.students.distinct('first_name')
docs3 = db.students.distinct('last_name')
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for x,y,z in zip(docs,docs2,docs3):
    print(f"Student ID: {x}")
    print(f"First Name: {y}")
    print(f"Last Name: {z}")
    print()

doc = db.students.find_one({"student_id": "1007"})
print("\n\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")

again = input("\n\nEnd of program, press any key to exit...")
if again:
  quit()
