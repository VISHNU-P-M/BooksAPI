# API for Books Inventory


Here you have Six APIs for creating new user, JWT authenticated login, Refresh token, Borrow a book, getting all books, getting details of specific book, and getting all books that user borrowed.
#### Call 'token/' POST API for creating jwt token.
#### Call 'token/refresh/' POST API for create access token by refresh token.
#### Call 'create-user/' POST API for creating a user.
#### Call 'all-books/' GET API for get all books.
#### Call 'details/<book_id>/ GET API for read the details of the book.
#### Call 'borrow-book/' GET API for get all book that user borrowed.
#### Call 'borrow-book/' POST API for borrow a book.

## Creating Environment

Create an environment on your system

```bash
Install virtual environment:
python -m pip install --user virtualenv

Creating new environment:
py -m venv env

Activate environment:
.\env\Scripts\activate
```

## Install all requirments

Install all package that needs to run this application

```bash
pip install requirements.txt 
```

## Run Application
First you need to migrate, create a super user for adding books

```bash
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```