from settings import *
import json

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), nullable= False)
    age = db.Column(db.Integer, nullable= True)
    tel = db.Column(db.Integer, nullable= False)
    classs = db.Column(db.String(50), nullable= False)

    def json(self):
        return {'id': self.id, 'name': self.name,
                'age': self.age, 'tel': self.tel, 'classs': self.classs
        }
    
    def add_student(_name, _age, _tel, _classs):
        new_student = Student(name= _name, age= _age, tel= _tel, classs= _classs)
        db.session.add(new_student)
        db.session.commit()

    def get_all_student():
        return [Student.json(student) for student in Student.query.all()]
    
    def get_student(_id):
        return [Student.json(Student.query.filter_by(id= _id).first())]
    
    def edit_student(_id, _name, _age, _tel, _classs):
        student_edit = Student.query.filter_by(id= _id).first()
        student_edit.name = _name
        student_edit.age = _age
        student_edit.tel = _tel
        student_edit.classs = _classs
        db.session.commit()
    
    def delete_student(_id):
        Student.query.filter_by(id= _id).delete()
        db.session.commit()
