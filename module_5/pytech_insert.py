#Lanedra Moore
#June 29, 2023
#CYBR410 Data/Database Security
#pytech_insert.py

#import
from pymongo import MongoClient

#connection string
url = "mongodb+srv://admin:admin@cluster0.ok0kjbr.mongodb.net/?retryWrites=true&w=majority"

#connect to cluster
client = MongoClient(url)

#connect database
db = client.pytech

#add student info
fred = {
    "student_id": "1007",
    "first_name": "Fred",
    "last_name": "Wiasley",
    "enrollments": [
        {
            "term": "Spring",
            "gpa": "4.0",
            "start_date": "06/10/2023",
            "end_date": "08/10/2023",
            "courses": [
                {
                    "course_id": "CIS245",
                    "description": "Introduction to Programming",
                    "instructor": "Joe Allan",
                    "grade": "A+"
                },
                {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security",
                    "instructor": "Joe Doe",
                    "grade": "A+"
                }
            ]
        }
        ]
}

george = {
    "student_id": "1008",
    "first_name": "George",
    "last_name": "Wiasley",
    "enrollments": [
        {
            "term": "Spring",
            "gpa": "3.4",
            "start_date": "06/10/2023",
            "end_date": "08/10/2023",
            "courses": [
                {
                    "course_id": "ART204",
                    "description": "Pottery",
                    "instructor": "Crea Tive",
                    "grade": "A"
                },
                {
                    "course_id": "MAT255",
                    "description": "Algebra I",
                    "instructor": "Suh Coh Toa",
                    "grade": "B-"
                }
            ]
        }
    ]
}

ron = {
    "student_id": "1009",
    "first_name": "Ron",
    "last_name": "Wiasley",
    "enrollments": [
        {
            "term": "Spring",
            "gpa": "2.9",
            "start_date": "06/10/2023",
            "end_date": "08/10/2023",
            "courses": [
                {
                    "course_id": "FLI455",
                    "description": "Introduction to Flying",
                    "instructor": "",
                    "grade": "B-"
                },
                {
                    "course_id": "DEF200",
                    "description": "Defense Against the Dark Arts",
                    "instructor": "Umbridget",
                    "grade": "D-"
                }
            ]
        }
    ]
}

#go to student collection
students = db.students

#insert statements
print("\n-- INSERT STATEMENTS -- ")
fred_student_id = students.insert_one(fred).inserted_id
print("Inserted student record Fred Wiasley into the students collection with document_id: " + str(fred_student_id))
george_student_id = students.insert_one(george).inserted_id
print("Inserted student record George Wiasley into the students collection with document_id: " + str(george_student_id))
ron_student_id = students.insert_one(ron).inserted_id
print("Inserted student record Ron Wiasley into the students collection with document_id: " + str(ron_student_id))

#end program
input("\n\nEnd of program, press any key to exit...")