import uuid
from src.common.database import Database
from flask import session

from src.models.menu import Menu

//creating the class for email and password
class Customer(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id
//returns the class for customer email
    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("customers", {"email": email})
        if data is not None:
            return cls(**data)
//returns the class for customer email_id 
    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("customers", {"_id": _id})
        if data is not None:
            return cls(**data)
// returns the class for customer email and password 
    @staticmethod
    def login_valid(email, password):
        # Check whether a user's email matches the password they sent us
        customer = Customer.get_by_email(email)
        if customer is not None:
            # Check the password
            return customer.password == password
        return False
// return the class and store it to database
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



// return the static for login
    @staticmethod
    def login(user_email):
        # login_valid has already been called
        session['email'] = user_email
// return the static for logout
    @staticmethod
    def logout():
        session['email'] = None



    def json(self):
        return {
            "email": self.email,
            "password": self.password
        }
// saving to the database
    def save_to_mongo(self):
        Database.insert("customers", self.json())


