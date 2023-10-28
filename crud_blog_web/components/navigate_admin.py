from django.contrib import admin
from ..models import Navigate


@admin.register(Navigate)
class NavigateAdmin(admin.ModelAdmin):
    fields = ['title', 'link']
    search_fields = ["title"]
