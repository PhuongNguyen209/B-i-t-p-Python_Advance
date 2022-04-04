import sqlalchemy as sa
from data.modelbase import ModelBase

class Company(ModelBase):
    __tablename__ = 'Company'

    id= sa.Column('Id', sa.Integer, primary_key= True, autoincrement= True)
    name= sa.Column('Name', sa.String, nullable= False)
    address= sa.Column('Address', sa.String, nullable= False)
    dkkd= sa.Column('DKKD', sa.Integer)
    date_of_regist= sa.Column('D_O_R', sa.Date)
    tel= sa.Column('Tel', sa.String, nullable= False)
    email= sa.Column('Email', sa.String)

    __table_args__ = (
        sa.Index('my_index','Name', 'Address', 'Tel'),
    )

    def __repr__(self):
        return f'<Company {self.id} {self.name} {self.address} {self.dkkd} {self.date_of_regist} {self.tel} {self.email}>'

