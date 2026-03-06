from src.configuration.open_config import MONGO_URL
from pymongo import MongoClient


client = MongoClient(MONGO_URL)
