from pymongo import MongoClient


client = MongoClient("mongodb://mongodb:27017/")
db = client["telegram_bot_db"]
users_collection = db["users"]
