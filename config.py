import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Base configuration
    SECRET_KEY = os.getenv('SECRET_KEY')  # Use the SECRET_KEY from .env
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Use the DATABASE_URL from .env
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')  # Default to 'production' if not set in .env

# Optionally, you can have different configurations for development and production like:
class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
