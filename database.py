import os
from pymongo import MongoClient

# MongoDB Connection
MONGO_URL = os.getenv("MONGO_URL", "your_mongo_url")
client = MongoClient(MONGO_URL)
db = client["TelegramBot"]
users_collection = db["Users"]

def add_user(user_id):
    """Add new user to database"""
    if not users_collection.find_one({"user_id": user_id}):
        users_collection.insert_one({"user_id": user_id})

def get_total_users():
    """Get total number of users"""
    return users_collection.count_documents({})
