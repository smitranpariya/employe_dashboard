from app import create_app, db
from app.models import Employee, Attendance, Performance
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_employee_data():
    employees = []
    for _ in range(5):  # Create 5 employees
        emp = Employee(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            position=fake.job(),
            hire_date=fake.date_this_decade()
        )
        db.session.add(emp)
        employees.append(emp)

    db.session.commit()

    # Create Attendance and Performance records for employees
    for employee in employees:
        attendance = Attendance(
            employee_id=employee.id,
            date=fake.date_this_year(),
            status=fake.random_element(elements=('Present', 'Absent', 'Vacation'))
        )
        performance = Performance(
            employee_id=employee.id,
            rating=fake.random_element(elements=(1, 2, 3, 4, 5)),
            feedback=fake.sentence()
        )
        db.session.add(attendance)
        db.session.add(performance)

    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        generate_employee_data()
    print("Synthetic data generated.")
