from app import create_app, db
from app.models import Employee, Attendance, Performance
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_employee_data(batch_size=50):
    employees = []
    attendance_records = []
    performance_records = []
    
    # Generate Employees
    for _ in range(batch_size):  # Create 50 employees at once
        emp = Employee(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            position=fake.job(),
            hire_date=fake.date_this_decade()
        )
        employees.append(emp)
    
    # Add employees to session
    db.session.add_all(employees)
    db.session.commit()  # Commit employees to DB before generating related data
    
    # Create Attendance and Performance records for employees
    for employee in employees:
        # Create Attendance records
        attendance = Attendance(
            employee_id=employee.id,
            date=fake.date_this_year(),
            status=fake.random_element(elements=('Present', 'Absent', 'Vacation'))
        )
        attendance_records.append(attendance)
        
        # Create Performance records
        performance = Performance(
            employee_id=employee.id,
            rating=fake.random_element(elements=(1, 2, 3, 4, 5)),
            feedback=fake.sentence()
        )
        performance_records.append(performance)

    # Add attendance and performance records to the session
    db.session.add_all(attendance_records)
    db.session.add_all(performance_records)
    
    # Commit all records (attendance + performance) to DB at once
    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        generate_employee_data(batch_size=50)
    print("Synthetic data generated for 50 employees.")
