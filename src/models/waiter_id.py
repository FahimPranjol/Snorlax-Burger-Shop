from src.common.database import Database
from flask import session

class Info(object) :
    def __init__ (self, table, waitstaff, _id=None):
        self.table = table
        self.waitstaff = waitstaff
        self._id = None


    @classmethod
    def get_table(cls, table):
        data = Database.find_one("infos", ("Table No.": table))
        if data is not None:
            return cls(**data)

    @classsmethod
    def get_waitstaff(cls, waitstaff):
        data = Databade.find_one("infos",("waitstaff": waitstaff))
        if data is not None:
            return clas(**data)

    @classmethod
    def new_assign(cls, table, waitstaff):
        assign = cls.get_table(table)

        if assign is None:
            new_assign = cls(table, waitstaff)
            new_assign.save_to_mongo()
            session['table_no'] = table
            session['waitstaff'] = waitstaff
            return True

        else:
            return False

    def save_to_mongo(self):
        Database.insert("infos", self.json())