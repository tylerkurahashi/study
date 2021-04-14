from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
print(client)

finace_db = client.finance
print(finace_db)
sum_collection = finace_db.sum
print(sum_collection)

history = sum_collection.find_one()
print(history)

@app.route('/')
def hello():
    return str(history['Income'])