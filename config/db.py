from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv("URI_DB")

conn = MongoClient(KEY)

print("connected to database")

db = conn.Dashboard
