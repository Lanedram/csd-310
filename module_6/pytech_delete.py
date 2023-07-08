#   Lanedra Moore
#   July 8, 2023
#   CYBR410 
#   pytech_queries.py : program to delete documents from collection
#   link to github: https://github.com/Lanedram/csd-310.git

#Import/Connect Database
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ok0kjbr.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

#connect student collection and find all students
students = db.students
student_list = students.find({})

#Display information
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")

#loop through the documents in the collection
for document in student_list:
    print(" Student ID: " + document["student_id"])
    print(" First Name: " + document["first_name"])
    print(" Last Name: " + document["last_name"])
    print()

#Add another student (Hermione Granger)
test_student = {
    "student_id": "1010",
    "first_name": "Hermione",
    "last_name": "Granger"
}

#Insert the student into the collection and print confirmation
test_student_id = students.insert_one(test_student).inserted_id

print("")
print(" -- INSERT STATEMENT -- ")
print("  Inserted student record into the students collection with document_id " + str(test_student_id))

#find student 1010 and print the results
test_student_doc = students.find_one({"student_id": "1010"})

print("\n\n -- DISPLAYING STUDENT TEST DOC -- ")
print(" Student ID: " + test_student_doc["student_id"])
print(" First Name: " + test_student_doc["first_name"])
print(" Last Name: " + test_student_doc["last_name"])
print("")

#remove the student, update list, and show the results of the whole collection
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

updated_student_list = students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")

for document in updated_student_list:
    print(" Student ID: " + document["student_id"])
    print(" First Name: " + document["first_name"])
    print(" Last Name: " + document["last_name"])
    print()

#exit the program with any key
input("\n\n End of program, press any key to continue...")



