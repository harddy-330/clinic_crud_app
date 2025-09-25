# 🏥 Clinic Booking API
![clinic](https://github.com/user-attachments/assets/d366c8f4-c54a-4974-a8f6-f63ea59dc87d)

A simple, clean, and scalable CRUD API for managing Patients and Appointments in a clinic system, built with **FastAPI** and **MySQL**.

---

## 🚀 Features

- ✅ Create, read, delete Patients
- ✅ Create, read Appointments
- ✅ FastAPI with automatic Swagger docs
- ✅ MySQL database with SQLAlchemy ORM
- ✅ `.env`-based config for security
- ✅ Modular project structure
- ✅ Easy to deploy and extend

---

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [MySQL](https://www.mysql.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📁 Project Structure



clinic_crud_app/
├── app/
│ ├── init.py
│ ├── main.py # FastAPI app & endpoints
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # DB logic functions
│ └── database.py # DB connection & session
├── .env # Environment variables (not committed)
├── .env.example # Example of environment config
├── requirements.txt # Dependencies
└── README.md


---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.10+
- MySQL server running
- Git installed

---

### 📦 1. Clone the Repo

```bash
git clone https://github.com/Langat1999/clinic_crud_app.git
cd clinic_crud_app

🔐 2. Configure .env

Create a .env file:

cp .env.example .env


Then edit .env with your actual database credentials:

DATABASE_URL=mysql+mysqlconnector://<username>:<password>@localhost/clinic_booking_system

📦 3. Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

🔧 4. Start MySQL & Create Database
CREATE DATABASE clinic_booking_system;


You can also use a .sql file if included.

▶️ 5. Run the App
uvicorn app.main:app --reload


Visit:

Swagger Docs: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

Root: http://localhost:8000/

🔌 API Endpoints
🧍 Patients
Method	Endpoint	Description
POST	/patients/	Create a new patient
GET	/patients/	List all patients
DELETE	/patients/{id}	Delete a patient
📅 Appointments
Method	Endpoint	Description
POST	/appointments/	Create an appointment
GET	/appointments/	List all appointments
📮 Example JSON Payloads
Create Patient
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "phone": "0700123456"
}

Create Appointment
{
  "patient_id": 1,
  "date": "2025-09-26T10:30:00",
  "notes": "Regular check-up"
}

🧪 Testing

You can use:

Postman

Swagger UI at /docs for live API testing

🔒 Security

.env file is excluded from version control using .gitignore

Never share production passwords or secrets

🤝 Contributing

Fork the repository

Create your feature branch (git checkout -b feat/your-feature)

Commit your changes (git commit -am 'Add feature')

Push to the branch (git push origin feat/your-feature)

Create a Pull Request

📄 License

This project is licensed under the MIT License
.

💬 Contact

Developed by Jackson Mutiso Langat
