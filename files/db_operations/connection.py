from pymongo import MongoClient

# Connection to the MongoDB server
cluster = MongoClient("mongodb+srv://admin:admin@101-dtcph.mongodb.net/test?retryWrites=true&w=majority")

# Connection to the database
db = cluster['palabras_encadenadas']

# Instances of the collections we are going to use
users = db['users']
dict = db['dictionaries']
games = db['games']
