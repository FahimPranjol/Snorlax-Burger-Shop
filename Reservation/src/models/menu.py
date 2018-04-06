import uuid

from flask import session

from src.common.database import Database


class Menu(object):
    def __init__(self, Item, price, _id=None):

        self.Item = Item
        self.price = price
        self._id = uuid.uuid4().hex if _id is None else _id


    def json(self):
        return {

            'Item': self.Item,
            'price': self.price,
            '_id': self._id
        }

    @classmethod
    def get_by_item(cls, item):

        item_name = Database.find_one("Menu", {"Item": item})
        if item_name is not None:
            return cls(**item_name)

    @staticmethod
    def item_valid(item):
        item_name = Menu.get_by_item(item)

        if item_name is not None:
            return True

        return False




    @staticmethod
    def menu(item):
        # login_valid has already been called
        session['Item'] = item



