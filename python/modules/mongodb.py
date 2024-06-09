import pymongo as pyM
import datetime

client = pyM.MongoClient("string")  # connects to the server

db = client.test
print(db.test_collection)

# Define document for mongodb
post = {
    "author": "Mike",
    "text": "My first mongodb app",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# Prepare to send the post
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
print(db.list_collection_names())
print(db.posts.find_one())

# Bulk insertions
new_posts = [
    {"author": "John",
     "text": "Hello from John",
     "tags": ["mongodb", "python3", "pymongo"],
     "date": datetime.datetime.utcnow()},
    {"author": "Mike",
     "text": "My second post",
     "title": "mongodb is flexible",
     "tags": ["mongodb", "python3", "pymongo"],
     "date": datetime.datetime.utcnow()}
]

result = posts.insert_many(new_posts)
print(result.inserted_ids)
pprint.pprint(db.posts.find_one({"author": "John"}))
