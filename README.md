<div align="center">

# 🚀 CodeGrader

**An automated online coding assignment platform built with Django & Django REST Framework**

Teachers create programming assignments with test cases. Students submit Python solutions and get instant, automated grading with detailed feedback.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-REST%20Framework-red?logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Production%20DB-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/Auth-JWT-000000?logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[Live Demo](#) · [Report Bug](../../issues) · [Request Feature](../../issues)

</div>

---

## 📖 Table of Contents

- [About](#-about)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [API Reference](#-api-reference)
- [Workflow](#-workflow)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 📌 About

CodeGrader is a full-stack coding assignment platform that automates the process of setting, submitting, and grading programming assignments. Teachers can create assignments with multiple hidden/visible test cases, deadlines, and marks. Students submit Python code that is automatically executed and evaluated, receiving instant per-test-case feedback and a leaderboard ranking.

The project exposes both a **server-rendered web UI** and a **complete REST API** (with JWT authentication), making it usable as a standalone web app or as a backend for a separate frontend/mobile client.

## 🌍 Live Demo

The project is deployed and publicly accessible.

🔗 **App URL:** `https://codegrader.up.railway.app` 

## ✨ Features

### 👨‍🏫 Teacher
- Secure teacher login with role-based authorization
- Create coding assignments with descriptions, deadlines, and marks
- Add multiple test cases (input/expected output) per assignment
- View all assignments and track submissions

### 👨‍🎓 Student
- Registration and login
- Browse available assignments
- Submit Python solutions through the web UI or API
- Automatic code execution against all test cases
- Instant grading with per-test-case pass/fail feedback
- Personal dashboard with submission statistics

### 📊 Dashboard
- Total submissions count
- Best score achieved
- Recent submission history

### 🏆 Leaderboard
- Ranking by highest score
- Live score updates as students submit

### 🔐 Authentication & Security
- Django's built-in authentication system
- Role-based access control (Teacher / Student)
- JWT authentication for the REST API
- Session authentication for the DRF Browsable API

### 🌐 REST API
A complete, browsable REST API built with Django REST Framework, supporting registration, login, assignment management, and submission/grading — all consumable by external clients (e.g. a React/Vue SPA or mobile app).

## 🛠 Tech Stack

| Layer          | Technology                                   |
|----------------|-----------------------------------------------|
| Backend        | Python, Django, Django REST Framework         |
| Database       | PostgreSQL (production), SQLite (local dev)   |
| Auth           | JWT (`djangorestframework-simplejwt`), Django Session Auth |
| Frontend       | Django Templates, HTML, CSS, JavaScript       |
| Styling        | Tailwind CSS, DaisyUI                          |
| Deployment     | Deployed to production (see [Live Demo](#-live-demo)) |

## 📸 Screenshots

| Assignment Dashboard | Submission Result | Submission History |
|:---:|:---:|:---:|
| *(screenshots/dashboard.png)* | *(screenshots/result.png)* | *(screenshots/history.png)* |

## 📂 Project Structure

```
codegrader/
│
├── accounts/          # User auth, registration, roles (teacher/student)
├── assignments/       # Assignment & test case models, views
├── submissions/       # Submission handling, code evaluation, grading
├── templates/         # Django HTML templates
├── theme/             # Tailwind CSS / DaisyUI theme config
├── manage.py
└── requirements.txt
```

## ⚙️ Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL (for production-like setup) or SQLite (quick local testing)
- `pip` and `venv`

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Unnati-29/CodeGrader.git
cd CodeGrader

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env   # then fill in your values (see below)

# 5. Apply migrations
python manage.py migrate

# 6. Create an admin/superuser account
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
```

Open your browser at:

```
http://127.0.0.1:8000/
```

## 🔑 Environment Variables

Create a `.env` file in the project root (do not commit this file):

```env
SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com

DATABASE_URL=postgres://user:password@host:port/dbname

JWT_ACCESS_TOKEN_LIFETIME_MINUTES=60
JWT_REFRESH_TOKEN_LIFETIME_DAYS=7
```

> Adjust variable names to match however `settings.py` is currently configured (e.g. if using `django-environ` or `python-decouple`).

## 🌐 API Reference

Base URL: `/api/`

| Endpoint                  | Method | Description                          | Auth Required |
|----------------------------|--------|----------------------------------------|:---:|
| `/api/auth/register/`      | POST   | Register a new user (student/teacher) | No |
| `/api/auth/login/`         | POST   | Log in, returns JWT tokens             | No |
| `/api/auth/profile/`       | GET    | Get logged-in user's profile           | Yes |
| `/api/assignments/`        | GET    | List all assignments                   | Yes |
| `/api/assignments/`        | POST   | Create a new assignment (teacher only) | Yes |
| `/api/submissions/`        | GET    | List submissions (own / all for teacher) | Yes |
| `/api/submissions/`        | POST   | Submit code for grading                | Yes |

**Authentication:** Include the JWT access token in requests:

```
Authorization: Bearer <access_token>
```

The API is also explorable via the **DRF Browsable API** in a web browser, and supports **Session Authentication** for that purpose.

## 🔄 Workflow

**Teacher**
1. Register / Login
2. Create an assignment
3. Add test cases, set deadline & marks
4. Students are notified / can view the assignment

**Student**
1. Register / Login
2. Browse available assignments
3. Submit Python code
4. Code is automatically executed and evaluated
5. Receive score & detailed per-test-case feedback
6. Leaderboard updates in real time

## 🗺 Roadmap

Planned enhancements for future releases:

- [ ] Containerized code execution sandbox (Docker) for safe/isolated code runs
- [ ] Redis + Celery for asynchronous grading
- [ ] Multi-language support (C++, Java, in addition to Python)
- [ ] Plagiarism detection
- [ ] Email notifications (new assignments, results)
- [ ] Assignment-level analytics for teachers
- [ ] Submission status states (Pending / Running / Accepted / Wrong Answer)
- [ ] Dedicated teacher dashboard with class-wide insights
- [ ] Student progress tracking over time

## 📌 Project Status

**Current Version:** v1.1

- ✅ Deployed to production
- ✅ PostgreSQL as the production database
- ✅ Template-based web application
- ✅ REST API (DRF)
- ✅ JWT authentication
- ✅ Role-based access control
- ✅ Automatic code evaluation
- ✅ Dashboard & leaderboard
- ✅ Assignment management

**In Progress / Upcoming**
- 🚧 Docker-based code execution sandbox
- 🚧 Multi-language compiler support
- 🚧 Advanced analytics

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add: your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please open an issue first to discuss significant changes.

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 👩‍💻 Author

**Unnati Raj**
Mechanical Engineering Undergraduate, NIT Silchar
Aspiring Software Development Engineer | Django · DRF · DSA · Web Development

[GitHub](https://github.com/Unnati-29) · [LinkedIn](https://www.linkedin.com/in/unnati-raj-354945368/) 
---

<div align="center">

If you found this project useful, consider giving it a ⭐ on GitHub!

</div>
