from pymongo import MongoClient
from phrases import PHRASES


client = MongoClient("mongodb://mongodb:27017/")
db = client["telegram_bot_db"]
users_collection = db["users"]
phrases_collection = db["phrases"]


def migrate_phrases():
    for phrase in PHRASES:
        if not phrases_collection.find_one(phrase):
            phrases_collection.insert_one({"phrase": phrase})
