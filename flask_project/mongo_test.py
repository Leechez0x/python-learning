from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
connection_string = os.getenv("MONGO_URI")

client = MongoClient(connection_string, tls=True, tlsAllowInvalidCertificates=True)

db = client["my_database"]
collection = db['students']

collection.delete_many({})

students = [
    {"name": "David", "country": "UK", "city": "London", "age": 34},
    {"name": "John", "country": "Sweden", "city": "Stockholm", "age": 28},
    {"name": "Sami", "country": "Finland", "city": "Helsinki", "age": 25},
]
collection.insert_many(students)
print('Students inserted!')

print('\nAll students in database:')
for student in collection.find():
    print(student)

collection.update_one({'name': 'David'},{'$set': {'age': 40}})
print("\nAfter updating David's age:")
for student in collection.find():
    print(student)

collection.delete_one({'name': "John"})
print('\nAfter deleting John:')
for student in collection.find():
    print(student)
