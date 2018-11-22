# MyTest.py
from MSSQL.Db_mg import DatabaseManagement
from MSSQL.Position import Position
from sqlalchemy import and_


class MyTest():
    def __init__(self):
        self.db_obj = DatabaseManagement()

    def process(self):
       #   person_obj = Position("james","22", 18)
       # person_obj = self.db_obj.add_obj(person_obj)
        query_filter = and_(Position.PositionName != "")
        person_list = self.db_obj.query_all(Position, query_filter)
        for i in person_list:
            print(i.PositionName+i.Description)


if __name__ == "__main__":
    myTest = MyTest()
    myTest.process()

