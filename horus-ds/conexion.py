import pymongo
 
from pymongo import MongoClient
 
Mongo_URI = "mongodb+srv://vaccine-devs:vaccine-devs123@clustervaccinedeveloper.imldj.mongodb.net/vaccine-devs?retryWrites=true&w=majority"

# conexión
cliente = MongoClient(Mongo_URI)

db = cliente["vaccine-devs"]
 
# colección
colec_vaccdata = db["vaccineData"]

 


