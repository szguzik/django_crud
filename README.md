
# Crud Django
### Instalacja

W celu zainstalowania Django należy wykonać polecenie 
```sh
pip install django
```
#### Po zainstalowaniu pakietu dostepna jest komenda `django-admin {polecenie}` oraz pakiet poleceń pliku manage.py

#### Teraz należy utworzyć projekt za pomocą polecenia
 `django-admin startproject {nazwa_projektu}`
```sh
django-admin startproject crud_blog .
```
#### Uruchomienie projektu odbywa się za pomocą polecenia
```sh
python manage.py runserver
```
#### Dodawanie aplikacji odbywa się za pomocą komendy `django-admin startapp {nazwa_app}`
```sh
django-admin startapp crud_blog_web
```
### UWAGA 
#### POLECENIE `django-admin startproject crud_blog .` tworzy projekt
#### POLECENIE `django-admin startapp crud_blog_web .` tworzy aplikację
#### PROJEKT MOŻE SKŁADAĆ SIĘ Z APLIKACJI

### Migracje
#### Migracje - lista rzeczy, które powinny być zaaplikowane do naszej bazy danych aby było możliwe jej używanie.
### Polecenie służące do wykonywania migracji
```sh 
python manage.py migrate
```
