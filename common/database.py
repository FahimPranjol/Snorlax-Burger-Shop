import pymongo

__author__ = 'jslvtr'


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)


    @staticmethod
    def delete(collection):
        Database.DATABASE[collection].remove({})



    @staticmethod
    def find(collection):
        return Database.DATABASE[collection].find({})

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update_one(collection, query, query2):
         Database.DATABASE[collection].update_one(query, query2)

    @staticmethod
    def update_many(collection, query, query2):
         Database.DATABASE[collection].update_many(query, query2)

    @staticmethod
    def replace_one(collection, query, query2):
         Database.DATABASE[collection].replace_one(query, query2)





