# freelancing-solutions  ![Build status](https://travis-ci.com/anshulahuja98/freelancing-solutions.svg?token=sxKTXczsK8R6uvz4sAHy&branch=master)
A freelancing platform project for course *CS223(Software Engineering)*

## A Web portal to act as an intermediary between Freelancers and Employers
### Purpose

This project includes:
- OAuth facilities(Register/Login) for Employers and Freelancers.
- A `jobs` module for handling jobs, bids and skills.
- An `admin` interface to handle data.

### Installation:
Requirements:
- Python 3 runtime
- Django 2.1.7
- Other dependencies in Pipfile

Procedure:
- Install [python](https://www.python.org/downloads/) in your environment.
- Navigate to the cloned repository.
    ```
    cd <project_directory_name>     # freelancing-solutions
    ```
- Install `pipenv` for dependency management
    ```
    pip install pipenv              # for any system with python environment
    ```
     OR
    ```
    brew install pipenv             # for MacOS
    ``` 
- Copy `.env.example` to `.env`
    ```
    cp .env.example .env            
    ```
- Use pipenv to install other dependencies from `Pipfile`
    ```
    pipenv install
    ```
- Change to `src` directory and optionally activate virtual environment, if you don't want to activate env, use `pipenv run` to run python scripts
    ```
    cd src
    source "$(pipenv --venv)"/bin/activate
    ```
- Make database migrations
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
- Create a superuser for admin access
    ```
    python manage.py createsuperuser
    ```
- Run development server on localhost
    ```
    python manage.py runserver
    ```
    