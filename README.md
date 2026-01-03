# 🎓 Student Registration System (Django REST API)

A backend-only **Student Registration System** built using **Django** and **Django REST Framework (DRF)**.  
This project exposes RESTful APIs to manage **Students**, **Courses**, and **Enrollments**.

It is designed to be consumed by frontend frameworks such as **React**, **Vue**, **Angular**, **Flutter**, or mobile applications.

---

## 🚀 Features

- Create, read, update, and delete students
- Manage courses with different levels
- Enroll students into courses
- Django Admin panel support
- RESTful API using Django REST Framework
- SQLite database (easy to replace with PostgreSQL/MySQL)
- Ready for Postman testing

---


## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yeab166/StudentRegistrationSystem.git
cd school-api-drf

```

```bash
python -m venv venv
venv\Scripts\activate   # For Windows

```

```bash
pip install -r requirements.txt

```


```bash
SECRET_KEY=your-secret-key-here
DEBUG=True

```

```bash
python manage.py makemigrations
python manage.py migrate

```


```bsh
python manage.py runserver

