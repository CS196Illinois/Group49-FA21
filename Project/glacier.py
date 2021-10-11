import pymongo

client = pymongo.MongoClient()
db = client.test

print(db)