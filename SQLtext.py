# MyTest.py
from db_mg import DatabaseManagement
from sqlServer import Person
from sqlalchemy import and_


class MyTest():
    def __init__(self):
        self.db_obj = DatabaseManagement()

    def process(self):
        person_obj = Person("james","22", 18)
        person_obj = self.db_obj.add_obj(person_obj)
        query_filter = and_(Person.PositionName == "james")
        person_list = self.db_obj.query_all(Person, query_filter)
        for i in person_list:
            print(i.PositionName)


if __name__ == "__main__":
    myTest = MyTest()
    myTest.process()

