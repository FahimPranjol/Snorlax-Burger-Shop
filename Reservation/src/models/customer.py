import uuid
from src.common.database import Database
from flask import session




class Customer(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("customers", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("customers", {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        # Check whether a user's email matches the password they sent us
        customer = Customer.get_by_email(email)
        if customer is not None:
            # Check the password
            return customer.password == password
        return False

    @staticmethod
    def login(user_email):
        # login_valid has already been called
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None



    def json(self):
        return {
            "email": self.email,
            "password": self.password
        }

    def save_to_mongo(self):
        Database.insert("customers", self.json())


