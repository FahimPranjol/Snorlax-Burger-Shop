import uuid
from src.common.database import Database
from flask import session

from src.models.menu import Menu


#creating customer object
class Customer(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    #getting customer by email
    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("customers", {"email": email})
        if data is not None:
            return cls(**data)

    #getting customer by id if ID is assigned
    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("customers", {"_id": _id})
        if data is not None:
            return cls(**data)
    #validating the user's email id and password
    @staticmethod
    def login_valid(email, password):
        # Check whether a user's email matches the password they sent us
        customer = Customer.get_by_email(email)
        if customer is not None:
            # Check the password
            return customer.password == password
        return False

    #registering the customer by asking for their information
    @classmethod
    def register(cls, email, password):
        customer = cls.get_by_email(email)
        if customer is None:
            # User doesn't exist, so we can create it
            new_customer = cls(email, password)
            new_customer.save_to_mongo()
            session['email'] = email
            return True
        else:
            # User exists :(
            return False



    #checking if login is succssfull
    @staticmethod
    def login(user_email):
        # login_valid has already been called
        session['email'] = user_email

    #logging out
    @staticmethod
    def logout():
        session['email'] = None


    #inserting data into the database as json
    def json(self):
        return {
            "email": self.email,
            "password": self.password
        }

    #saving information to the database
    def save_to_mongo(self):
        Database.insert("customers", self.json())


