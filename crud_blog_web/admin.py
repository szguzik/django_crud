from django.contrib import admin
from .models import Article


# Register your models here.
# admin.site.register(Article)

# Użycie klasy Admin jako dekorator
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # deklaracja pól, które mają zostac pokazane
    # W przypadku, kiedy nie ma trego pola oznacza to zgodę na wyświetlenie wszystkich pól
    fields = ["title", "content", "year", "imgThumb"]

    # Exclude - deklaracja pól, których nie chcemy używać
    # exclude = ["content"]

    # Deklaracja reprezentacji obiektu po stronie panelu
    # Metoda __str__ definiuje, jak obiekt modelu powinien być przedstawiony
    # jako łańcuch znaków. Jest ona używana w wielu miejscach,
    # w tym w interfejsie użytkownika panelu administracyjnego Django,
    # ale nie w głównym widoku listy, na który wpływa list_display.
    list_display = ["title", "year"]

    # Dodawanie filtra w panelu w tym przypadku po roku
    list_filter = ["year"]

    # Analogiczny zapis zale jak używasz tuple to pamiętaj o dodaniu przecinka na koniec nawiasu
    # list_filter = ("year",)

    # Dodanie wyszukiwarki po stronie panelu wraz z deklaracją pól do przeszukiwania
    search_fields = ["title", "content"]
