from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250, blank=False, unique=False)
    content = models.TextField(default='')
    year = models.PositiveSmallIntegerField(default=2023)

    def __str__(self):
        return self.title + ' (' + str(self.year) + ')'

