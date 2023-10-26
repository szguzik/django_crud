from django.contrib import admin
from django.urls import path, include
from crud_blog_web.views import test_response
from django.conf import settings
from django.conf.urls.static import static
from crud_blog_web.views import all_articles

urlpatterns = [
    path('', all_articles),
    path('admin/', admin.site.urls),
    path('test/', test_response),
    path('crud-blog/', include("crud_blog_web.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
settings.MEDIA_URL: W Django, MEDIA_URL to ustawienie, które definiuje bazowy publiczny adres URL 
dla plików mediów przesłanych przez użytkowników. Może to być coś w stylu '/media/'.

settings.MEDIA_ROOT: Jest to bezwzględna ścieżka w systemie plików do katalogu, 
w którym przechowywane są pliki mediów przesłane przez użytkowników. 
Na przykład może to być coś takiego jak '/sciezka/do/twojego/projektu/media/'.

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT): 
Funkcja static() jest funkcją pomocniczą używaną w urls.py 
w Django do serwowania plików statycznych podczas deweloperki 
(czyli podczas lokalnego tworzenia i testowania aplikacji, a nie na produkcji). 
Umożliwia ona serwowanie plików zdefiniowanych w MEDIA_ROOT pod adresem URL zdefiniowanym w MEDIA_URL.

https://docs.djangoproject.com/en/4.2/howto/static-files/#s-serving-static-files-during-development
'''
