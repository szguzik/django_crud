from django.urls import path
from crud_blog_web.views import all_articles
urlpatterns = [
    path('test/', all_articles),
]
