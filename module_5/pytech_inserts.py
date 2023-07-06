from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.2pmbegp.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
fred = {
    "first_name": "Fred",
    "last_name": "Flintstone",
    "student_id": "1007"
}
fred_student_id = db.students.insert_one(fred).inserted_id

barney = {
    "first_name": "Barney",
    "last_name": "Rubble",
    "student_id": "1008"
}
barney_student_id = db.students.insert_one(barney).inserted_id

george = {
    "first_name": "George",
    "last_name": "Slate",
    "student_id": "1009"
}
george_student_id = db.students.insert_one(george).inserted_id

print("-- Insert Statements --")
print(f"Inserted student record Fred Flintstone into the students collection with document_id {fred_student_id}")
print(f"Inserted student record Barney Rubble into the students collection with document_id {barney_student_id}")
print(f"Inserted student record George Slate into the students collection with document_id {george_student_id}")
again = input("\n\nEnd of program, press any key to exit...")
if again:
  quit()
