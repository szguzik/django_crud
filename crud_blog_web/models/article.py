from django.db import models


# Create your models here.
class Article(models.Model):
    # Pole objects w tym modelu służy do pobierania obiektów z tabeli Articles
    # Domyślnie ustawione na None
    objects = None
    # Pole title - ilość znaków 250, pole nie może być puste,  pole nie musi być unikalne
    title = models.CharField(max_length=250, blank=False, unique=False)
    # Pole content przyjmuje dowolną ilośc znaków, domyślnie ustawia pusty string
    content = models.TextField(default='')
    # Pole year (zakres jest zwykle od 1 do 32767), oraz ustawiona domyślna wartość 2023
    year = models.PositiveSmallIntegerField(default=2020)
    imgThumb = models.ImageField(upload_to="media_img", null=True, blank=True)

    '''
    W kontekście modeli Django, magiczna metoda __str__ jest często używana do
    zapewnienia przyjaznej dla użytkownika reprezentacji obiektu modelu,
    która może być używana w panelu administracyjnym Django, szablonach czy logach.
    '''
    def __str__(self):
        return self.title_with_year()

    # Metoda do łączenia  pola title z polem year z użyciem metody format
    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)
