from pymongo import MongoClient
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
#print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#print("date and time =", dt_string)
#def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
 #  CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
  # client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   #return client['user_shopping_list']
  
# This is added so that many files can reuse the function get_database()
#if __name__ == "__main__":   
  
   # Get the database
  # dbname = get_database()

CONNECTION_STRING = "localhost"
client = MongoClient(CONNECTION_STRING)
db = client["RASPBERRY_DATABASE"]

#print(db.list_collection_names())

row=   { "plate_number" : '1233DC33',
        "time_in" : now,
        "time_out" : ""}

collection = db.get_collection('LICENSEPLATE_NAME')
collection.insert_one(row)

#print(collection.find({}))
cursor = collection.find({})
for document in cursor:
          print(document)