#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/4/29 11:18
# @Author : russell
# @File :  testSQLAlchemy

# sqlite:////absolute/path/to/foo.db

from sqlalchemy import Column, String, create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 初始化引擎
engine = create_engine('sqlite:///test.db', pool_size=20, max_overflow=0, poolclass=QueuePool)

#
Base = declarative_base()

# table
class User(Base):
    __tablename__ = 'user'
    id = Column(String(30), primary_key=True)
    name = Column(String(30))


# Base.metadata.create_all(engine)


def dbconnect(func):
    def inner(*args, **kwargs):
        DBsession = sessionmaker(bind=engine)
        ses = DBsession()
        try:
            func(*args, session=ses, **kwargs)
            ses.commit()
            print("提交成功")
        except:
            ses.rollback()
            # log
        finally:
            ses.close()
    return inner



@dbconnect
def add(session):
    new = User(id='4', name='Basdasdbb')
    session.add(new)



add()


