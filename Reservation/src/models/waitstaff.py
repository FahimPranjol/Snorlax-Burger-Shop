import uuid
from src.common.database import Database
from flask import session

#declaring class for the waitstaff by thier username and password
class Waitstaff(object):
    def __init__(self, username, password, _id=None):
        self.username = username
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id  # usually going to have an id when created

    #getting the waitstaff information from the database by id
    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("staff", {"_id": _id})
        if data is not None:
            return cls(**data)

    # getting the waitstaff information from the database by username
    @classmethod
    def get_by_username(cls, username):
        data = Database.find_one("staff", {"username": username})
        if data is not None:
            return cls(**data)

    #validating the username and password of the waitstaff
    @staticmethod
    def valid_login(username, password):
        staff = Waitstaff.get_by_username(username)
        if staff is not None:
            return staff.password == password
        return False

    #checking if the login is successful
    @staticmethod
    def login(username):
        session['username'] = username

    #checking for successful logout
    @staticmethod
    def logout():
        session['username'] = None

    #connecting to the data base
    def json(self):
        return{
            "username": self.username,
            "password": self.password,
            "_id": self._id
        }

    #saving to mongodb database
    def save_to_mongo(self):
        Database.insert("staff", self.json())
