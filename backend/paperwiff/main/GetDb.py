from flask import g
from pymongo import MongoClient


def get_db():
    client = MongoClient(
        "mongodb://localhost:27017"
    )
    db = client["paperwiff-new"]
    return db


def close_db(e=None):
    if g.mongo_client is not None:
        g.mongo_client.close()