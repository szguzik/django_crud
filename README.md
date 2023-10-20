
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
### Tworzenie super użytkownika
```sh
python manage.py createsuperuser
```
Dla potrzeb projektu wprowadzone dane to:
```sh
Username: xman
Email: szymon.guzik@gdansk.merito.pl
Password: qwerty2023
```

### Uzupełenienie modelu
W aplikacji `crud_blog_web` znajduje się plik `models.py`. 
Plik ten należy uzupełnić w celu wygenerowanie na jego podstawie migracji
```shell
class Article(models.Model):
    title = models.CharField(max_length=64)
```
ten zapis oznacza, że pole title będzie miało długość 64 znaków


### Tworzenie migracji na podstawie modelu
```sh
python manage.py makemigrations
```
Została wygenerowana migracja w lokalizacji
`crud_blog_web -> mogrations` <br>
Teraz należy wykonać ponownie migracje za pomocą polecenia
```sh 
python manage.py migrate
```
Aby aplikacja była widoczna w panelu admina należy ją zarejestrować w admin.py <br>
Lokalizacja pliku `crud_blog_web`
```sh
from django.contrib import admin
from .models import Article
# Register your models here.
admin.site.register(Article)
```
### Aktualizacja modelu oraz wskazanie co ma sie wyswietlic w czasie pobierania modelu
```sh
class Article(models.Model):
    title = models.CharField(max_length=250, blank=False, unique=False)
    content = models.TextField(default='')
    year = models.PositiveSmallIntegerField(default=2023)

    def __str__(self):
        return self.title
```
Ponowne wykoonanie poleceń do migracji w celu aktualizacji bazy
```sh
python manage.py makemigrations
python manage.py migrate
```

Dodanie pola do wgrywania mediów
```sh
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250, blank=False, unique=False)
    content = models.TextField(default='')
    year = models.PositiveSmallIntegerField(default=2023)
    imgThumb = models.ImageField(upload_to="media_img", null=True, blank=True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)
```
### Zarządzanie polami w adminie
Dodanie dekoratora oraz klasy ArticleAdmin
```sh
from django.contrib import admin
from .models import Article


# Register your models here.
# admin.site.register(Article)

# Użycie klasy Admin jako dekorator
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
```

Deklaracja używanych pól
```sh
fields = ["title", "content", "year", "imgThumb"]
```
Deklaracja wykluczonych pól
```sh
exclude = ["content"]
```
Deklaracja reprezentacji po stronie panelu admina (deklaracja listy)
```sh
list_display = ["title", "year"]
```
Dodawanie filtra w panelu w tym przypadku po roku
```sh
list_filter = ["year"]
```
Dodanie wyszukiwarki po stronie panelu wraz z deklaracją pól do przeszukiwania
```sh
search_fields = ["title", "content"]
```
### Tworzenie adresów WWW (path)
Plik `urls.py z projektu a nie aplikacji`
```sh
from django.contrib import admin
from django.urls import path
from crud_blog_web.views import test_response
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_response),
]
```
W widoku aplikacji (`views.py  aplikacji`)
```sh
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def test_response(request):
    return HttpResponse("To jest przykładowy url")

```
#### Tworzenie adressów na poziomie aplikacji (oddzielanie od głównego pliku z adresami)
1. Stworzenie pliku `urls.py` w APLIKACJI
2. Dopisanie routingu
```sh
from django.urls import path
from crud_blog_web.views import test_response
urlpatterns = [
    path('test/', test_response),
]
```
3. Dodanie obsługi routingu w pliku `urls.py` PROJEKTU np. (`path('crud-blog/', include("crud_blog_web.urls"))`)
```sh
from django.contrib import admin
from django.urls import path, include
from crud_blog_web.views import test_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_response),
    path('crud-blog/', include("crud_blog_web.urls")),
```
### Linki
Dokumentacja - [Dokumentacja 4.2](https://docs.djangoproject.com/en/4.2/)  
Rodzaje pól - [Pola dla modeli](https://docs.djangoproject.com/en/4.2/ref/models/fields/)
