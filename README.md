# django-trees-everywhere
This project was created with Django 5.0.2.

## Create a virtual environment
Run ```python3 -m venv``` to create a python virtual environment on your current directory. Run ```source venv/bin/activate``` to activate it. If you're on Windows, run ```source venv/Scripts/activate```.

## Install dependencies
Execute ```pip install -r requirements.txt``` to install all of the project dependencies.

## Create you environment variable
Create a file named ```.env``` and fill it as the ```.env.example``` file indicates.

## Run Migrations
Run ```python manage.py migrate``` to execute all pending migrations. This project is set to work with SQLite by default, so the database will be created automatically on the folder of your project.

## Run fixtures
There's a Tree fixture already available. Run ```python manage.py loaddata tree_fixture.json``` to load some data into your Tree table.

## Create Super User
Run ```python manage.py createsuperuser``` to set an super user admin profile for your application. Follow the steps on the terminal and the user will be created.

## Run the application
Run ```python manage.py runserver``` and the project will be served on a port of your localhost. Access the ```/admin``` route and login as the superuser you have created. There you will be able to manage the data for your tables and add new users. Access the ```/tree``` route to view the application. Login as one of the users you have created on the admin interface.
