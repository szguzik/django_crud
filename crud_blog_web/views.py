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
