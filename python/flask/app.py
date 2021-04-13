from flask import Flask
from pymongo import MongoClient
import pymongo

app = Flask(__name__)
client = MongoClient()

@app.route('/')
def hello():
    return "Hello, World!"