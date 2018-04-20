import uuid

import datetime
from flask import session

from src.common.database import Database


class Tables(object):
    def __init__(self, table_no, table_name, user_email, coupon, date=datetime.datetime.now(), _id=None):

        self.table_no = table_no
        self.coupon=coupon
        self.table_name = table_name
        self.user_email = user_email
        self.created_date = date
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection="tables", data=self.json())

    def json(self):
        return{

            'table_no': self.table_no,
            'coupon':self.coupon,
            'table_name': self.table_name,
            'user_email': self.user_email,
            'created_date': self.created_date,
            '_id':self._id
        }
