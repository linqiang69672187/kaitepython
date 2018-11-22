from sqlalchemy import Column,String,INT
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()    #创建对象的基类
class Person(Base):          #定义一个类，继承Base
    __tablename__='Position'
    ID = Column(INT(),primary_key = True)
    PositionName = Column(String(50))
    Description = Column(String(100))
    Weight = Column(INT())

    def __init__(self,PositionName,Description,Weight):
        self.Description=Description
        self.PositionName = PositionName
        self.Weight = Weight
