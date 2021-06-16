# Medicento Payment Tracker CRM API

This project is a django REST framework based API providing API endpoints for Medicento Payment Tracker App.

## Local Setup

To run locally, do the usual:

1. Fork this repo to your github account, clone your github repo.
2. Create a Python 3.8 virtualenv, activate your virtualenv.
3. Install dependencies:
    > pip install -r requirements.txt
4. Create database:
    > python manage.py migrate
5. Create superuser:
    > python manage.py createsuperuser
6. Run local server:
    > python manage.py runserver