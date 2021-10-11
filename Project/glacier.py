import pymongo

client = pymongo.MongoClient("mongodb+srv://Viven:<Group49>@glacier.cxwbq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

print(db)