from pymongo import MongoClient


DATABASE_URL = "mongodb://nraboy:password1234@localhost:27017"

client = MongoClient(DATABASE_URL)
