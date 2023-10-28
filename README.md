
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
#### Tworzenie adresów na poziomie aplikacji (oddzielanie od głównego pliku z adresami)
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
### Templates
1. Deklaracja templates w pliku konfiguracyjnym PROJEKTU (`settings.py`)
```sh
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        ...
    },
]
```
2. Tworzenie katalogu tempates w głównym katalogu
- crud_blog
- crud_blog_web
- templates
- venv

3. W katalogu pliku z urls.py (Aplikacja lub Projekt) dodanie metody do wybranego route
4. W pliku `views.py` APLIKACJI dodanie metody z, która była wskazana w punkcie wyżej np.
```sh
from django.shortcuts import render
...
def all_articles(request):
    title_page = "To jest tytuł strony"
    return render(
        request,
        'articles.html',
        {'title': title_page}
    )
```
5. Stworzenie w katalogu `templates` pliku `articles.html` i dodać kod html 
```sh
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <!--Ta wartość została przekazana z widoku - views.py w aplikacji-->
    <h1>{{ title }}</h1>
    <h2>Tutaj będą moje artykuły</h2>
</body>
</html>
```
Za pomocą `{ klucz_wartości }` zostaje przekazana wartość z pliku `aplikacja\views.py` - przykład w kodzie wyżej

Poniższy przykład pokazuje pobieranie danych z bazy, dodanie opcji statycznych oraz stringa  
Plik `views.py`
```sh
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.
def test_response(request):
    return HttpResponse("To jest przykładowy url")


def all_articles(request):
    title_page = "To jest tytuł strony"
    options = [
        "option 1",
        "option2",
        "option3"
    ]

    articles = Article.objects.all()

    return render(
        request,
        'articles.html',
        {
            'title': title_page,
            'options': options,
            'articles': articles
        }
    )

```
Plik `articles.html`
```sh
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <!--Ta wartość została przekazana z widoku - views.py w aplikacji-->
    <h1>{{ title }}</h1>
    <h2>Tutaj będą moje artykuły</h2>
    <h3>To są opcje ustawione statycznie</h3>
    {% for item in options %}
    <p>{{ item }}</p>
    {% endfor %}
    <h3>To są artykuły pobrane z bazy za pomocą modelu - bez koniecznosci wskazywania na property</h3>
    <h4>Nie musimy wskazywać property bo w modelu naszej aplikacji jest </h4>
    <pre>
        <code>
            def __str__(self):
              return self.title_with_year()

        </code>
    </pre>
    <b>Przykład iteracji bez wskazywania na właściwość (property)</b>
    {% for article in articles %}
    <p>{{ article }}</p>
    {% endfor %}

    <b>Przykład iteracji ze wskazaniem właściwości (property)</b>
    {% for article in articles %}
    <p>{{ article.title }}</p>
    {% endfor %}

</body>
</html>
```

### CDN Bootstrap
```sh
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Document</title>
</head>
...
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

</body>
```

### ORM w Django
Pobieranie wpisów o konkretnym tytule  
```sh
articles = Article.objects.get(title="Testowy")
```
lub  
```sh
articles = Article.objects.get(id=1)
```
Pobieranie wpisów o konkretnym tytule (tutaj będzie błąd i program się wysypie)  
```sh
articles = Article.objects.get(title="Testowy2nieIstnieje")
```
Pobieranie wpisów o konkretnym tytule (Nic nie zostanie znalezione ale sie nie wysypie)  
```sh
articles = Article.objects.filter(title="Testowy2nieIstnieje")
```
Pobieranie wpisów o konkretnym tytule (filter zwraca tylko znalezione wpisy)  
```sh
articles = Article.objects.filter(title="Testowy")
```
Tworzenie nowych wpisów np. z konsole ale można tego też używać w kodzie
```sh
Article.objects.create(title="Wpis z konsoli", year=2024, content="Tresc wprowadzona z konsoli") 
```
Kasowanie za pomocą wywołania metowy delete (technika  "łańcuchowanie metod" (ang. method chaining))  
```sh
articles = Article.objects.get(id=1).delete()
```

### Pliki statyczne
w `settings.py` projektu należy odszukać lub dodać deklaracje
```sh
STATIC_URL = 'static/'
# Static directories (Global)
STATICFILES_DIRS = ['assets']
```
W tablicy `STATICFILES_DIRS` są dodane katalogi zawierające pliki statyczne np pliki css, js, media
W stringu `STATIC_URL` jest zdeklarowany prefix zawierający nazwę "lokalizacji" dla naszego plikiem 

W głównym katalogu aplikacji należy utworzyć katalog `assets` a w nim plik statyczny np. `styles.css`
```
project-blog
|- /assets/
|  |-styles.css
```
Na samym początku szablonu np. `articles.html` trzeba zdeklarować używanie plików statycznych
```sh
{% load static %}
<!doctype html>
```
Używanie plików sstatycznych zostaje wywołane w następujący sposób
```sh
<link rel="stylesheet" href="{% static 'styles.css' %}">
```
Pliki statyczne można również deklarować wewnątrz aplikacji w katalogu static
```
project-blog
|- /crud_blog_web/
|  |-/static/
|  | |-crud_blog_web.css
```
Wczytywanie ich idbywa się w analogiczny sposób ale aby zobaczyć elekty należy zrestartować serwer
```sh
<link rel="stylesheet" href="{% static 'crud_blog_web.css' %}">

```
### Wyświetlanie zdjęć

W `settings.py` projektu należy ustawić
```sh
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'
```
Następnie w szyblonie (np `articless.html`) dodac wywołanie zdjęcia ze wskazaniem katalogu prefixowego (`media`)  
Taki jest właśnie zadeklarowany "dwie linijki wyżej"
```sh
<img src="/media/{{ article.imgThumb }}" alt="{{ article.title }}" title="{{ article.title }}">
```



### Linki
Dokumentacja - [Dokumentacja 4.2](https://docs.djangoproject.com/en/4.2/)  
Rodzaje pól - [Pola dla modeli](https://docs.djangoproject.com/en/4.2/ref/models/fields/)  
Statyczne URL - [Statyczne Pola](https://docs.djangoproject.com/en/4.2/howto/static-files/#s-serving-static-files-during-development)
