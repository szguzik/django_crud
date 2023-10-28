from django.db import models


# Create your models here.
class Navigate(models.Model):
    objects = None
    title = models.CharField(max_length=250, blank=False, unique=False)
    link = models.TextField(default='', blank=True)

    def __str__(self):
        return self.title_with_link()

    def title_with_link(self):
        return "{} (/{})".format(self.title, self.link)