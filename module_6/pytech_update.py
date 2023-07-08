#   Lanedra Moore
#   cybr410 
#   07/08/2023
#   pytech_update.py : program to update documents in pytech collection

#import/connect database
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

#update student_id 1007 to a different last name
students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Weasley"}})

#find the student who was updated
fred = students.find_one({"student_id": "1007"})

#display results
print("")
print(" -- DISPLAYING STUDENT DOCUMENT 1007 -- ")
print(" Student ID: " + fred["student_id"])
print(" First Name: " + fred["first_name"])
print(" Last Name: " + fred["last_name"])
print()

#exit program with the click of a key
input("\n  End of program, press any key to continue... ")