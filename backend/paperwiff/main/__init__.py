from flask import g
from pymongo import MongoClient


def get_db():
    client = MongoClient(
        "mongodb://localhost:27017"
    )
    db = client["paperwiffdb-beta"]
    return db


def close_db(e=None):
    if g.mongo_client is not None:
        g.mongo_client.close()


# INITIALIZE TAGS COLLECTION
# availableTags = [
#     "Fiction",
#     "Action & Adventure",
#     "Crime",
#     "Drama",
#     "Fairytale",
#     "Historical Fiction",
#     "Horror",
#     "Mystery",
#     "Paranormal Romance",
#     "Poetry",
#     "Romance",
#     "Sattire",
#     "Science Fiction",
#     "Suspense",
#     "Thriller",
#     "Non-Fiction",
#     "Art",
#     "Biography",
#     "Book review",
#     "Guide",
#     "Travel",
#     "Health",
#     "History",
#     "Memoir",
#     "Spirituality",
#     "Self-Help",
#     "Politics",
#     "Shayari"
# ]
# db = get_db()
# tags = db['tags']
# for tag in availableTags:
#     tags.insert_one({"name": tag.lower().replace(" ", ""), 'status': False})
