import os
import data.db_session as db_session
from data.company import Company
from sqlalchemy import or_, and_

def setup_db():
    db_file= os.path.join(os.path.dirname(__file__), 'db', 'Company.sqlite')
    db_session.global_init(db_file)

def print_result(result):
    for entry in result:
        print(entry)

def query_all(ses):
    for company in ses.query(Company):
        print(company)

def query_equals(ses):
    for company in ses.query(Company).filter(Company.id == 1):
        print(company)

def query_not_equals(ses):
    for company in ses.query(Company).filter(Company.id != 1):
        print(company)

def query_greater_than(ses):
    for company in ses.query(Company).filter(Company.id > 3):
        print(company)

def query_like(ses):
    for company in ses.query(Company).filter(Company.name.like("Co%C")):
        print(company)

if __name__ == '__main__':
    setup_db()

    session= db_session.factory()

    print("---All---")
    query_all(session)

    print("---equals---")
    query_equals(session)

    print("---Not equals---")
    query_not_equals(session)

    print("---Greater---")
    query_greater_than(session)
    
    print("---Like---")
    query_like(session)

    print("Close session!")
    session.close()