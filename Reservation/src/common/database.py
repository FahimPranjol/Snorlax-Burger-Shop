import pymongo

__author__ = 'jslvtr'

//creating the class 
class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None
//connecting to the database
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']
//inserting the data from database
    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)
//collecting the data from database
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)




