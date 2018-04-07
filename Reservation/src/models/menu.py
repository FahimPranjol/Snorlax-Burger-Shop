import uuid

from flask import session

from src.common.database import Database


class Menu(object):
    def __init__(self, Item, price, _id=None):

        self.Item = Item
        self.price = price
        self._id = uuid.uuid4().hex if _id is None else _id




    @classmethod
    def get_by_item(cls, item):

        item_name = Database.find_one("Menu", query={"Item": item})
        return cls(**item_name)

    @staticmethod
    def item_valid(item):
        item_name = Menu.get_by_item(item)

        if item_name is not None:
            return True

        return False




    @classmethod
    def item_add(cls,name, price):
        # login_valid has already been called
        new_item = cls(name, price)
        new_item.save_to_mongo()


    def json(self):
        return{

            "Item":self.Item,
            "price":self.price

        }

    def save_to_mongo(self):
        Database.insert("order",self.json())



