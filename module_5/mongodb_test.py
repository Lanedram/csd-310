
   # Lanedra Moore
   # June 29, 2023
   # Test program for connecting to Atlas
   # mongodb_test.py

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ok0kjbr.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print("\n -- Pytech Collection List --")
print(db.list_collection_names())

input("\n\n   End of program, press any key to exit...")