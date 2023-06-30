
   # Lanedra Moore
   # June 29, 2023
   # Test program for connecting to Atlas
   # mongodb_test.py

#import
from pymongo import MongoClient

#connection string
url = "mongodb+srv://admin:admin@cluster0.ok0kjbr.mongodb.net/?retryWrites=true&w=majority"

#connect to cluster
client = MongoClient(url)

#connect database
db = client.pytech

#show collections
print("\n -- Pytech Collection List --")
print(db.list_collection_names())

#exit message
input("\n\n   End of program, press any key to exit...")