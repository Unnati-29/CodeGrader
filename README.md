# CodeGrader 🚀

A full-stack Django-based online coding assignment platform where teachers can create programming assignments and students can submit solutions that are automatically evaluated against predefined test cases.

---

## ✨ Features

### 👨‍🏫 Teacher

* Teacher login and authentication
* Role-based authorization
* Create coding assignments
* Add multiple test cases
* Set deadlines and marks
* View all assignments

### 👨‍🎓 Student

* Student registration & login
* View available assignments
* Submit Python solutions
* Automatic code execution
* Instant grading
* Detailed feedback for each test case
* Dashboard with submission statistics

### 📊 Dashboard

* Total submissions
* Best score
* Recent submissions

### 🏆 Leaderboard

* Ranking based on highest scores
* Live score updates

### 🔐 Authentication

* Django Authentication
* Role-based access (Teacher / Student)
* JWT Authentication for REST API
* Session Authentication for Browsable API

### 🌐 REST API

Complete REST API built using Django REST Framework.

Available endpoints:

```
/api/auth/register/
/api/auth/login/
/api/auth/profile/

/api/assignments/
/api/submissions/
```

Supports:

* GET
* POST
* Retrieve
* Authentication with JWT
* Browsable API

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* SQLite
* Tailwind CSS
* DaisyUI
* JWT Authentication
* HTML
* CSS
* JavaScript

---

## Project Structure

```
codegrader/
│
├── accounts/
├── assignments/
├── submissions/
├── templates/
├── theme/
├── manage.py
└── requirements.txt
```

---

## Current Workflow

### Teacher

* Register/Login
* Create Assignment
* Add Test Cases
* Students receive assignment

### Student

* Register/Login
* View Assignments
* Submit Python Code
* Automatic Evaluation
* Receive Score & Feedback
* Leaderboard Updates

---

## API Testing

The REST API has been tested using:

* Django REST Framework Browsable API
* JWT Authentication
* Session Authentication

Verified workflows:

* User Registration
* User Login
* Assignment Creation
* Assignment Listing
* Code Submission
* Automatic Grading
* Dashboard API
* Leaderboard API

---

## Screenshots

### Assignment Dashboard



![Dashboard](screenshots/dashboard.png)



### Submission Result



![Result](screenshots/result.png)



### Submission History



![History](screenshots/history.png)

---

## Future Improvements

* Docker Deployment
* PostgreSQL
* Redis + Celery
* Asynchronous Code Execution
* Code Execution Sandbox (Docker)
* Multi-language Support (C++, Java, Python)
* Plagiarism Detection
* Email Notifications
* Assignment Analytics
* Submission Status (Pending / Running / Accepted / Wrong Answer)
* Teacher Dashboard
* Student Progress Tracking

---

## Installation

```bash
git clone https://github.com/Unnati-29/CodeGrader.git

cd CodeGrader

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## Project Status

**Current Version:** v1.0

✔ Template-based Web Application

✔ REST API (DRF)

✔ JWT Authentication

✔ Role-Based Access Control

✔ Automatic Code Evaluation

✔ Dashboard

✔ Leaderboard

✔ Assignment Management

🚧 Upcoming

* Deployment
* Docker Sandbox
* Multi-language Compiler
* Advanced Analytics

---

## Author

**Unnati Raj**

Mechanical Engineering Undergraduate, NIT Silchar

Aspiring Software Development Engineer | Django | DRF | DSA | Web Development

