from pymongo import MongoClient

conn = MongoClient("mongodb+srv://admin_ayrton:Noty2015@cluster0.xsrqy.mongodb.net/?retryWrites=true&w=majority")

print("connected to database")

db = conn.Dashboard
