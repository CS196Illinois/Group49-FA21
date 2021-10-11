import pymongo

#MongoDB
client = pymongo.MongoClient()
db = client.test

print(db)