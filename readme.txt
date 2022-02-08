https://stackabuse.com/creating-a-rest-api-with-django-rest-framework/

python3 -m venv env

. env/bin/activate
cd ireligram


pip3 install django
pip3 install djangorestframework

django-admin startproject ireligram

python3 manage.py migrate
python3 manage.py createsuperuser

python3 manage.py makemigrations