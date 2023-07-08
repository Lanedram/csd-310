#   Lanedra Moore
#   July 8, 2023
#   CYBR410 
#   pytech_queries.py : program to delete documents from collection

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

