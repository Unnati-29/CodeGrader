# CodeGrader

CodeGrader is an assignment management and automated grading platform built using Django and Tailwind CSS. It enables instructors to create assignments and test cases, while providing a foundation for automated code evaluation and instant feedback.

## Features

### Authentication
- User Registration & Login
- Role-Based Authentication (Teacher / Student)
- Secure Logout

### Assignment Management
- Create Assignments (Teacher Only)
- View Assignment List
- Assignment Details

### Code Submission
- Submit Python Solutions
- Automatic Code Evaluation
- Instant Score & Feedback

### Dashboard
- Student Dashboard
- Best Score
- Total Submissions
- Recent Submission History

### Leaderboard
- Score-based Ranking
- User-wise Total Scores

### Modern UI
- Responsive Tailwind CSS Interface
- DaisyUI Components

## Upcoming Features

- Teacher Dashboard
- Submission Status (Accepted/Wrong Answer)
- Multiple Hidden Test Cases
- Monaco Code Editor
- Assignment Difficulty Levels
- Assignment Deadlines
- Search & Filter
- Student Profiles
- REST API
- Docker-based Secure Code Execution

## Screenshots

### Assignment Dashboard

![Dashboard](screenshots/dashboard.png)

### Submission Result

![Result](screenshots/result.png)

### Submission History

![History](screenshots/history.png)

## Tech Stack

* Python
* Django
* SQLite
* Tailwind CSS
* DaisyUI

## Project Structure

```text
CodeGrader/
│
├── assignments/
├── submissions/
├── templates/
├── static/
├── theme/
├── codegrader/
│
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone <repository-url>
cd CodeGrader

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

## Current Status

🚧 Under Development

🚀 MVP Completed

### Completed
- Assignment Management
- Test Case Management
- Student Code Submission
- Automated Code Evaluation
- Instant Feedback & Scoring
- Submission History
- Leaderboard
- User Authentication (Register/Login/Logout)

### In Progress
- Role-Based Access Control
- Home Page & Navigation Improvements
- Deployment
