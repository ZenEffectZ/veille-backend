## Installation pour Mac/Linux

Requis:
python, virtualenv

NOTE: Selon la version et la façon que Python est installé, il faut utiliser python/pip ou python3/pip3 pour les commandes.

###Créer un environnement virtuel:
#### Version 1:
virtualenv env
#### Activer l'environnement:
source env/bin/activate


#### Version 2:

python3 -m venv env
#### Activer l'environnement:
. env/bin/activate

alternative:

cd env

cd bin | cd Scripts

./activate

### Installer les modules:
pip3 install -r requirements.txt


### Démarrer le serveur:

python3 manage.py runserver

# medium

https://medium.com/django-rest/django-rest-framework-b3028b3f0b9

python3 manage.py migrate
python3 manage.py createsuperuser

python3 manage.py makemigrations
virtualenv env
source venv/bin/activate

|-----------------------------|---------|----------------------|
| ENDPOINT                    | METHOD  | ACTION               |
|-----------------------------|---------|----------------------|
| products/                   | GET     | list()               |
| products/:pk                | GET     | retrieve()           |
| products/get_list           | GET     | get_list()           |
| products/get_product/:pk    | GET     | get_product()        |
| products/delete_product/:pk | DELETE  | delete_product()     |
| products/delete_product/:pk | POST    | delete_product()     |
|-----------------------------|---------|----------------------|

/profile

voir posts, edit

coucou
coucou123

jakepaul
jakepaul123