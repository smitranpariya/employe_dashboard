import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2
from dotenv import load_dotenv
from flasgger import Swagger

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
swagger = Swagger() 

def create_app():
    # Load environment variables from .env file
    load_dotenv()

    # Initialize Flask app
    app = Flask(__name__)

    

    # Get the DATABASE_URL directly from the environment
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://localhost/employee_dashboard')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'supersecretkey')  # Default secret key if not set in .env

    # Extract database name from the DATABASE_URL (e.g., "employee_database")
    database_url = app.config['SQLALCHEMY_DATABASE_URI']
    database_name = database_url.split('/')[-1]

    app.config['SWAGGER'] = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }

    # Initialize Swagger ONCE
    swagger.init_app(app)

    # Connect to PostgreSQL server to check if the database exists
    try:
        # Connect to the 'postgres' database to check for the existence of 'employee_database'
        conn = psycopg2.connect(
            database='postgres',  # Connect to the default 'postgres' database
            host='localhost',
            port='5432',
            user=os.getenv('DB_USER', 'postgres'),  # Use the credentials from DATABASE_URL
            password=os.getenv('DB_PASSWORD', 'password')
        )
        conn.autocommit = True  # Enable autocommit to run CREATE DATABASE
        cursor = conn.cursor()

        # Check if the database exists
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname='{database_name}'")
        if not cursor.fetchone():
            print(f"Database '{database_name}' does not exist, creating it...")
            cursor.execute(f"CREATE DATABASE {database_name}")
        
        cursor.close()
        conn.close()

    except psycopg2.OperationalError as e:
        print(f"Error connecting to the database: {e}")
        return None

    # Now set the proper DATABASE_URL for SQLAlchemy to connect to the correct database
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER', 'postgres')}:{os.getenv('DB_PASSWORD', 'password')}@localhost:5432/{database_name}"

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Create tables if they don't exist
    try:
        with app.app_context():
            db.create_all()  # This will create all the tables in the database if they don't already exist.
    except Exception as e:
        print(f"Error creating tables: {e}")
        return None

    # Register routes (assuming you have a blueprint setup)
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    # Return the Flask app instance
    return app

# This is the script to run, add to generate_data.py
if __name__ == "__main__":
    app = create_app()
    if app is not None:
        with app.app_context():
            print("Flask app created successfully!")
