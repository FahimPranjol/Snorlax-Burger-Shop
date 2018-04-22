import uuid
from src.common.database import Database
from flask import session


class Order(object):
    def __init__(self, item_name, price, table, orders, table_name):
        self.item_name = item_name
        self.price = price
        self.table = table
        self.orders = orders
        self.table_name = table_name

    def json(self):
        return{
            'item_name': self.item_name,
            'price': self.price,
            'table': self.table
            'kstaff_orders': self.orders
            'table_name': self.table_name,
        }

    @classmethod
    def find_orders(cls, table):
        orders = Database.find(collection='orders',
                               query={'table': table})
        return[cls(**order) for order in orders]

    if (tableNo == "Table 1"):
        i = Database.find("table1_orders")

    elif (tableNo == "Table 2"):
        i = Database.find("table2_orders")

    elif (tableNo == "Table 3"):
        i = Database.find("table3_orders")

    elif (tableNo == "Table 4"):
        i = Database.find("table4_orders")

    elif (tableNo == "Table 5"):
        i = Database.find("table5_orders")

    elif (tableNo == "Table 6"):
        i = Database.find("table6_orders")

    elif (tableNo == "Table 7"):
        i = Database.find("table7_orders")

    elif (tableNo == "Table 8"):
        i = Database.find("table8_orders")

    elif (tableNo == "Table 9"):
        i = Database.find("table9_orders")

    elif (tableNo == "Table 10"):
        i = Database.find("table10_orders")

    elif (tableNo == "Table 11"):
        i = Database.find("table11_orders")

    elif (tableNo == "Table 12"):
        i = Database.find("table12_orders")

    elif (tableNo == "Table 13"):
        i = Database.find("table13_orders")

    elif (tableNo == "Table 14"):
        i = Database.find("table14_orders")

    elif (tableNo == "Table 15"):
        i = Database.find("table15_orders")

    elif (tableNo == "Table 16"):
        i = Database.find("table16_orders")
