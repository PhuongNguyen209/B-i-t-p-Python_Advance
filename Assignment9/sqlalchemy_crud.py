from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy import insert, delete, select

connection_string= "sqlite:///machine.db"
engine= create_engine(connection_string, echo= False)

metadata= MetaData()
computer= Table('Computer', metadata,
                Column('Id', Integer(), primary_key= True, autoincrement= True),
                Column('year', Integer()),
                Column('price', String),
                Column('owner', String),
                )

def do_select():
    s= computer.select()
    conn= engine.connect()
    result= conn.execute(s)

    for row in result:
        print(row)

def do_insert():
    stmt= computer.insert().values(
        year= '2020',
        price= '10000$',
        owner= 'an'
    )
    new_id= 0

    with engine.connect() as con:
        result= con.execute(stmt)
        new_id= result.inserted_primary_key['Id']
        print(f"New Id: {new_id}")
    
    return new_id

def selected_by_id(id):
    stmt= computer.select().where(computer.c.Id == id)
    with engine.connect() as con:
        result= con.execute(stmt).first()
        if result:
            print(result)
        else:
            print(f"No rows found id: {id}")

def do_delete(id):
    stmt= computer.delete().where(computer.c.Id == id)
    with engine.connect() as con:
        con.execute(stmt)
    print('Computer deleted!')

if __name__ == '__main__':
    print('---Get all computer---')
    do_select()

    print('---Insert new_computer---')
    id= do_insert()
    selected_by_id(id)

    print('---Delete computer---')
    do_delete(id)
    selected_by_id(id)

    print('---Completed!---')
