# CodeGrader

CodeGrader is an assignment management and automated grading platform built using Django and Tailwind CSS. It enables instructors to create assignments and test cases, while providing a foundation for automated code evaluation and instant feedback.

## Features

### Implemented

* Assignment Management

  * Create assignments
  * View assignment list
  * View assignment details

* Test Case Management

  * Create and manage test cases
  * Link test cases to assignments

* Teacher Interface

  * Assignment creation through web forms
  * Assignment browsing dashboard

* Modern UI

  * Built with Tailwind CSS
  * Responsive and clean design

## Upcoming Features

* Student code submission portal
* Automatic code evaluation
* Instant scoring and feedback
* Leaderboard and rankings
* Role-based authentication
* REST API integration
* Submission history tracking

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

Completed:

* Django project setup
* Assignment module
* Test case module
* Tailwind CSS integration
* Assignment dashboard

In Progress:

* Submission module
* Automated grading engine
* Teacher dashboard enhancements
