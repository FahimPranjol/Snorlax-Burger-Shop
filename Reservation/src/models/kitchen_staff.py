import uuid
from src.common.database import Database
from flask import session

#creating the kitchenstaff order
class Order(object):
    def __init__(self, item_name, price, table):
        self.item_name = item_name
        self.price = price
        self.table = table

    #inserting data into the database as json
    def json(self):
        return{
            'item_name': self.item_name,
            'price': self.price,
            'table': self.table
        }


    #finding orders by table number
    @classmethod
    def find_orders(cls, table):
        orders = Database.find(collection='orders',
                               query={'table': table})
        return[cls(**order) for order in orders]
