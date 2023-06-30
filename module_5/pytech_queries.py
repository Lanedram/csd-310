#   Lanedra Moore
#   June 30, 2023
#   Program to get something out of student collection
#   pytech_queries.py

#Import/Connect Database
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ok0kjbr.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

#connect student collection and find all students
students = db.students
student_list = students.find({})

#Show you found the students
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#each student document information in the student_list collection
for document in student_list:
    student_id = document["student_id"]
    first_name = document["first_name"]
    last_name = document["last_name"]
    print("Student ID: " + student_id + "\n First Name:" + first_name + "\n Last Name: " + last_name + "\n")

#using the find_one query option -- going to find ron
ron = students.find_one({"student_id": "1009"})
print("\n -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print(" Student ID: " + ron["student_id"] + "\n First Name: " + ron["first_name"] + "\n Last Name: " + ron["last_name"])

#leave the program
input("\n\n End of program, press any key to continue...")