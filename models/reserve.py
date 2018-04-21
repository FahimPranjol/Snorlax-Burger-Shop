from src.common.database import Database
from flask import session

class Info(object):
    def __init__(self, name, date, time, _id=None):
        self.date = date
        self.time = time
        self.name = name
        self._id = None

    @classmethod
    def get_date(cls, date):
        data = Database.find_one("infos", {"date": date})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_name(cls, name):
        data = Database.find_one("infos", {"name": name})
        if data is not None:
            return cls(**data)
    @classmethod
    def get_time(cls):
        data = Database.find_one("infos", {"time":cls.time})
        if data is not None:
           return cls(**data)

    @classmethod
    def new_reservation(cls,name, date, time):
        reserve = cls.get_date(date)


        if reserve is None:
            new_reserve = cls(name, date, time)
            new_reserve.save_to_mongo()
            session['name'] = name
            session['date'] = date
            session['time'] = time
            return True

        else:
            return False


    def json(self):
        return{

            "date":self.date,
            "time":self.time

        }

    def save_to_mongo(self):
        Database.insert("infos",self.json())
