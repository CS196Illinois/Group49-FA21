from pymongo import MongoClient
import json

# Making a Connection
myclient = MongoClient("mongodb+srv://Viven:Group49@glacier.cxwbq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") 
   
# creating the database
db = myclient["Factors"]
   
# Creating the collection
Collection = db["Snowfall in millimeters"]
  
# Opening the json file
with open('/Users/Viven/Group49-FA21/Project/Data/snowfall.json') as file:
    file_data = json.load(file)
      
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else inser_one is used
if isinstance(file_data, list):
    Collection.insert_many(file_data)  
else:
    Collection.insert_one(file_data)


"""# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient("mongodb+srv://Viven:Group49@glacier.cxwbq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# Set the db object to point to the business database
db=client.business
# Showcasing the count() method of find, count the total number of 5 ratings 
print('The number of 5 star reviews:')
fivestarcount = db.reviews.find({'rating': 5}).count()
print(fivestarcount)
# Now let's use the aggregation framework to sum the occurrence of each rating across the entire data set
print('\nThe sum of each rating occurance across all data grouped by rating ')
stargroup=db.reviews.aggregate(
# The Aggregation Pipeline is defined as an array of different operations
[
# The first stage in this pipe is to group data
{ '$group':
    { '_id': "$rating",
     "count" : 
                 { '$sum' :1 }
    }
},
# The second stage in this pipe is to sort the data
{"$sort":  { "_id":1}
}
# Close the array with the ] tag             
] )
# Print the result
for group in stargroup:
    print(group)"""

"""
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient("mongodb+srv://Viven:Group49@glacier.cxwbq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.business
#Step 2: Create sample data
names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
for x in range(1, 501):
    business = {
        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'rating' : randint(1, 5),
        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
    }
    #Step 3: Insert business object directly into MongoDB via insert_one
    result=db.reviews.insert_one(business)
    #Step 4: Print to the console the ObjectID of the new document
    print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
print('finished creating 500 business reviews')
"""

"""
#MongoDB
client = pymongo.MongoClient("mongodb+srv://Viven:<Group49>@glacier.cxwbq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

print(db)
"""