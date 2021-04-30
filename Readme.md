Polstats Setup
==============

$ python3 -m pip install virtualenv 

$ python3 -m venv yourenv       # Where "yourenv" is the name of your virtual environment

$ git clone https://github.com/ignaoya/polstats-django.git

$ source path/to/venv/yourenv/bin/activate      # To open virtual env

$ pip install -r requirements.txt

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py createsuperuser # To be able to login in localhost:8000/admin

$ python manage.py runserver


#If you are having database problems, delete the database, delete de migrations inside /migrations, and run the makemigrations and migrate commands again (warning: all your users and data will be deleted)