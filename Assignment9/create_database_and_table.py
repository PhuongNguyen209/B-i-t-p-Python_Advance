from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine= create_engine('sqlite:///machine.db', echo= False)
meta= MetaData()

computer= Table('Computer', meta,
                Column('Id', Integer(), primary_key= True, autoincrement= True),
                Column('year', Integer()),
                Column('price', String),
                Column('owner', String),
                )

meta.create_all(engine)


conn= engine.connect()
conn.execute(computer.insert(),[
    {'year': '2000', 'price': '1000$', 'owner': 'Phuong'},
    {'year': '2001', 'price': '2000$', 'owner': 'Hoang'},
    {'year': '2002', 'price': '3000$', 'owner': 'Son'},
    {'year': '2003', 'price': '4000$', 'owner': 'Duong'},
    {'year': '2004', 'price': '5000$', 'owner': 'Su'},
])