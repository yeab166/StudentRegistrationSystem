# 🎓 Student Registration System (Django REST API)

A backend-only **Student Registration System** built using **Django** and **Django REST Framework**, following a clean and modular architecture inspired by modern backend design.

This project provides RESTful APIs to register and manage students and is suitable for integration with frontend frameworks like **React**, **Vue**, **Flutter**, or **mobile apps**.

---

## 🚀 Features

- Student registration (Create)
- Fetch all students (Read)
- Clean MVC-style folder structure
- Django REST Framework based API
- SQLite database (easy to switch to PostgreSQL/MySQL)
- Ready for production deployment (WSGI enabled)

---

## 🏗️ Project Structure


  backend/
  │
  ├── app.py # Project entry point (like manage.py)
  ├── requirements.txt # Python dependencies
  │
  ├── config/ # Django project configuration
  │ ├── init.py
  │ ├── settings.py # Project settings
  │ ├── urls.py # Main URL routing
  │ └── wsgi.py # WSGI entry for deployment
  │
  ├── models/ # Database models
  │ ├── init.py
  │ └── student.py
  │
  ├── controllers/ # API logic (views)
  │ ├── init.py
  │ └── student_controller.py
  │
  ├── routes/ # API routes
  │ ├── init.py
  │ └── student_routes.py
