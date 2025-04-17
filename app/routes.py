from flask import Blueprint, jsonify, render_template
from .models import db, Employee, Attendance, Performance
from datetime import datetime

bp = Blueprint('routes', __name__)

# Get Employee Data
@bp.route('/employees', methods=['GET'])
def get_employees():
    """
    Get all employees
    ---
    responses:
      200:
        description: A list of all employees
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
              first_name:
                type: string
              last_name:
                type: string
              email:
                type: string
              position:
                type: string
              hire_date:
                type: string
                format: date
    """
    employees = Employee.query.all()
    return jsonify([{
        'id': employee.id,
        'first_name': employee.first_name,
        'last_name': employee.last_name,
        'email': employee.email,
        'position': employee.position,
        'hire_date': str(employee.hire_date)
    } for employee in employees])


# Get Attendance Data
@bp.route('/attendance', methods=['GET'])
def get_attendance():
    """
    Get all attendance records
    ---
    responses:
      200:
        description: A list of attendance records
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
              date:
                type: string
                format: date
              status:
                type: string
              employee_id:
                type: integer
    """
    attendance = Attendance.query.all()
    return jsonify([{
        'id': record.id,
        'date': str(record.date),
        'status': record.status,
        'employee_id': record.employee_id
    } for record in attendance])


# Get Performance Data
@bp.route('/performance', methods=['GET'])
def get_performance():
    """
    Get all performance records
    ---
    responses:
      200:
        description: A list of performance records
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
              rating:
                type: number
              feedback:
                type: string
              employee_id:
                type: integer
    """
    performance = Performance.query.all()
    return jsonify([{
        'id': record.id,
        'rating': record.rating,
        'feedback': record.feedback,
        'employee_id': record.employee_id
    } for record in performance])


# Generate synthetic employee data
@bp.route('/generate_data', methods=['POST'])
def generate_data():
    """
    Generate synthetic employee data
    ---
    responses:
      200:
        description: Synthetic data generated successfully
        schema:
          type: object
          properties:
            message:
              type: string
    """
    from generate_data import generate_employee_data
    generate_employee_data()
    return jsonify({'message': 'Synthetic data generated successfully!'})

@bp.route('/visualization')
def visualization():
    # Sample data retrieval from your database
    performance_data = Performance.query.all()

    # Format data for the chart
    data = {
        'names': [record.employee.first_name for record in performance_data],
        'scores': [record.rating for record in performance_data]
    }

    return render_template('visualization.html', data=data)
