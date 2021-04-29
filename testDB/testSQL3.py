import sqlite3

conn=sqlite3.connect('test.db')
cursor=conn.cursor()


cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

print(f'插入的行数: {cursor.rowcount}')


cursor.close()
conn.commit()

conn.close()


from testDB.testSQLAlchemy import dbconnect,User

@dbconnect
def addd(session):
    new = User(id='5', name='Basdasdbb')
    session.add(new)



addd()


