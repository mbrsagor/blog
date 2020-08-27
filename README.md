# Django Blog App

### Project Setup

###### Dependencies
- Python 3.8
- Django 3.1

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

### Download or clone the project 
Open your terminal then run the command ``git clone https://github.com/mbrsagor/blog/``

#### Create a python virtual environment:
Then install and create virtualenv in your project directory and active the virtualenv. `` Then follow the command

```
virtualenv venv --python=python3.8
source venv bin/active
```
After that run the project on your local development server. Please you may follow the commands. Hopefully It's will 
be work.

```
pip install -r requirements.txt
./ manage.py migrate
./ manage.py createsuperuser
./ manage.py runserver
```

<p>N:B: The project as a instractor I'm teaching my brothers and friends. They love to python and like to Django web 
application development.
</p>
