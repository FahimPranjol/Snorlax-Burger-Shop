import uuid

import datetime
from flask import session

from src.common.database import Database


class Table_order(object):
    def __init__(self, table_no, table_name, user_email, item, price, order_status, date=datetime.datetime.utcnow(), _id=None):

        self.table_no = table_no
        self.order_status = order_status
        self.item = item
        self.price = price
        self.table_name = table_name
        self.user_email = user_email
        self.created_date = date
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_table1(self):
        Database.insert(collection="table1_orders", data=self.json())

    def save_to_table2(self):
        Database.insert(collection="table2_orders", data=self.json())

    def save_to_table3(self):
        Database.insert(collection="table3_orders", data=self.json())

    def save_to_table4(self):
        Database.insert(collection="table4_orders", data=self.json())

    def save_to_table5(self):
        Database.insert(collection="table5_orders", data=self.json())

    def save_to_table6(self):
        Database.insert(collection="table6_orders", data=self.json())

    def save_to_table7(self):
        Database.insert(collection="table7_orders", data=self.json())

    def save_to_table8(self):
        Database.insert(collection="table8_orders", data=self.json())

    def save_to_table9(self):
        Database.insert(collection="table9_orders", data=self.json())

    def save_to_table10(self):
        Database.insert(collection="table10_orders", data=self.json())

    def save_to_table11(self):
        Database.insert(collection="table11_orders", data=self.json())

    def save_to_table12(self):
        Database.insert(collection="table12_orders", data=self.json())

    def save_to_table13(self):
        Database.insert(collection="table13_orders", data=self.json())

    def save_to_table14(self):
        Database.insert(collection="table14_orders", data=self.json())

    def save_to_table15(self):
        Database.insert(collection="table15_orders", data=self.json())

    def save_to_table16(self):
        Database.insert(collection="table16_orders", data=self.json())


    def save_to_waitstaff_page(self):
        Database.insert(collection="waitstaff_orders", data=self.json())



    def json(self):
        return{

            'table_no': self.table_no,
            'table_name': self.table_name,
            'user_email': self.user_email,
            'item':self.item,
            'price':self.price,
            'order_status':self.order_status,
            'created_date': self.created_date,
            '_id':self._id
        }
