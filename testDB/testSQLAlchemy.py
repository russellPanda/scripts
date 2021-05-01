#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/4/29 11:18
# @Author : russell
# @File :  testSQLAlchemy

# sqlite:////absolute/path/to/foo.db

from functools import wraps
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


def db_connect(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global engine
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

    return wrapper



@db_connect
def add(session):
    new = User(id='29', name='asdsadBasdasdbb')
    session.add(new)


add()
