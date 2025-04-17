from datetime import datetime
from . import db

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    position = db.Column(db.String(100))
    hire_date = db.Column(db.DateTime, default=datetime.utcnow)
    attendance = db.relationship('Attendance', backref='employee', lazy=True)
    performance = db.relationship('Performance', backref='employee', lazy=True)

    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'

class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)

class Performance(db.Model):
    __tablename__ = 'performance'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    feedback = db.Column(db.String(500))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
