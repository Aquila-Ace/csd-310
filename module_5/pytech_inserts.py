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

wilma = {
    "first_name": "Wilma",
    "last_name": "Flintstone",
    "student_id": "1008"
}
wilma_student_id = db.students.insert_one(wilma).inserted_id

pebbles = {
    "first_name": "Pebbles",
    "last_name": "Flintstone",
    "student_id": "1009"
}
pebbles_student_id = db.students.insert_one(pebbles).inserted_id

print("-- Insert Statements --")
print(f"Inserted student record Fred Flintstone into the students collection with document_id {fred_student_id}")
print(f"Inserted student record Wilma Flintstone into the students collection with document_id {wilma_student_id}")
print(f"Inserted student record Pebbles Flintstone into the students collection with document_id {pebbles_student_id}")
again = input("\n\nEnd of program, press any key to exit...")
if again:
  quit()
