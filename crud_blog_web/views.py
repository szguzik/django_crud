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

    # Pobieranie wpisów o konkretnym tytule
    #articles = Article.objects.get(title="Testowy")

    # Pobieranie wpisów o konkretnym tytule (tutaj będzie błąd i program się wysypie)
    #articles = Article.objects.get(title="Testowy2nieIstnieje")

    # Pobieranie wpisów o konkretnym tytule (Nic nie zostanie znalezione ale sie nie wysypie)
    #articles = Article.objects.filter(title="Testowy2nieIstnieje")

    # Pobieranie wpisów o konkretnym tytule (filter zwraca tylko znalezione wpisy)
    #articles = Article.objects.filter(title="Testowy")

    return render(
        request,
        'articles.html',
        {
            'title': title_page,
            'options': options,
            'articles': articles
        }
    )
