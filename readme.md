# Calorie Counter Web Application

A full-stack Django web application that helps users track their daily calorie intake. Add food items, view total calories, and maintain a healthy diet with this user-friendly calorie tracking tool.

## Features

- Add Food Items - Easily add food items with their calorie counts
- View Food Log - See all food items added for the current day
- Delete Items - Remove individual food items from your log
- Calculate Total - Automatically calculates total calories consumed for the day
- Reset Day - Clear all food items for a fresh start
- Responsive Design - Works on desktop, tablet, and mobile devices
- Real-time Updates - Instant calorie total calculation

## Technology Stack

- Backend: Django 4.2.7 (Python 3.x)
- Database: SQLite (Development) / PostgreSQL (Production)
- Frontend: HTML5, CSS3, Tailwind CSS
- Icons: Font Awesome 6
- Version Control: Git
- Deployment: Render

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup Instructions

1. Clone the repository
```bash
git https://github.com/maxmillan45/calorie_counter_project.git
cd calorie-counter
Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

```bash
pip install -r requirements.txt
Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
Create a superuser (optional)

```bash
python manage.py createsuperuser
Run the development server

```bash
python manage.py runserver
