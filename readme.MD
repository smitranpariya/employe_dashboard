# 🧑‍💼 Employee Analytics API

A Flask-based RESTful API for managing employees, tracking attendance and performance, with visualization and Swagger documentation support.

---

## 🚀 Features

- 🏗️ Modular Flask app structure
- 📊 Visual charts for performance & attendance using `matplotlib`
- 👥 Employee, Attendance & Performance models
- 🧪 Synthetic data generation using `Faker`
- 📄 Swagger UI for interactive API docs
- 🗃️ PostgreSQL database integration
- 📁 .env configuration for environment variables
- 📋 Logging support for debugging

---

## 📁 Project Structure

employe_dashboard/ 
    ├── app/ │ 
    ├── init.py │ 
    ├── models.py │ 
    ├── routes.py │ 
 ├── templates/ 
 │ └── visualization.html 
 ├── generate_data.py 
 ├── run.py 
 ├── .env 
 ├── requirements.txt
└── README.md

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/employe_dashboard.git
cd employe_dashboard

### 2. Create Virtual Enviroment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

### 3. Install neccessary dependancies

pip install -r requirements.txt

### create .env file in your root folder
employe_dashboard/ 
            ├── .env 

### 4 . configure .env file

FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost/dbname
SECRET_KEY=your-secret-key
DB_PASSWORD=password

### 5 . generate synthetic data

python generate_data.py

###6 . Run the Application

python run.py

## 7. Swagger API Docs

http://localhost:5000/apidocs/

###8 . visualization

http://localhost:5000/visualization



