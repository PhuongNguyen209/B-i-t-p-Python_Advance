import os
import data.db_session as db_session
from data.company import Company

def setup_db():
    db_file= os.path.join(os.path.dirname(__file__), 'db', 'Company.sqlite')
    db_session.global_init(db_file)

def create_data(ses):
    ses.add_all([
        Company(name = 'CommanyA', address = 'HN', tel = '000000'),
        Company(name = 'CommanyB', address = 'SG', tel = '111111'),
        Company(name = 'CommanyC', address = 'Hue', tel = '222222'),
        Company(name = 'CommanyD', address = 'HN', tel = '333333'),
        Company(name = 'CommanyE', address = 'HN', tel = '444444')
    ])
    ses.commit()
    print("Add database successful!")


def add_company(ses):
    company= Company()
    company.name = 'CompanyF'
    company.address= 'HaiPhong'
    company.tel= '555555'

    ses.add(company)
    ses.commit()
    print(company)

    return company.id

def load_company(id, ses):
    company= ses.query(Company).filter(Company.id == id).first()
    print(company)

def update(id, ses):
    company= ses.query(Company).filter(Company.id == id).first()
    print(company)
    company.address= 'Kontum'
    ses.commit()

    print(company)
    print('Update successful!')

def delete_company(id, ses):
    company= ses.query(Company).filter(Company.id == id).first()
    print(company)
    ses.delete(company)
    ses.commit()

if __name__ == '__main__':
    setup_db()
    session= db_session.factory()

    create_data(session)

    id= add_company(session)

    print("---Load company added")
    load_company(id, session)

    print("---Update company---")
    update(id, session)

    print("---Delete---")
    delete_company(id, session)
    print('Delete successful!')
    load_company(id, session)

    print('---Close session---')
    session.close()

