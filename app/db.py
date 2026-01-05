# db.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["pdf_extractor"]
collection = db["documents"]
