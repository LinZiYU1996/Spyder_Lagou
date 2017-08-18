#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/13 20:46
# @File    : Model.py


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer,Text
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:1996112lin@localhost:3306/mydata?charset=utf8')

Base = declarative_base()

class Job2(Base):
    __tablename__ = 'job2'
    id = Column(Integer, primary_key=True)
    companyFullName = Column(Text, nullable=False, index=True)
    workYear = Column(Text, nullable=False)
    salary = Column(Text, nullable=False, index=True)
    city = Column(Text, nullable=False, index=True)
    education = Column(Text, nullable=False, index=True)
    district = Column(Text, nullable=True, index=True)
    firstType = Column(Text, nullable=False, index=True)


    def __init__(self,list):
            self.companyFullName=list[0]
            self.workYear=list[1]
            self.salary=list[2]
            self.city=list[3]
            self.education=list[4]
            self.district=list[5]
            self.firstType=list[6]



