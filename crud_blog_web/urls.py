from django.urls import path
from crud_blog_web.views import test_response
urlpatterns = [
    path('test/', test_response),
]
