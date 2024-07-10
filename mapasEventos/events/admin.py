from django.contrib import admin
from .models import Event

# Register your models here.

class ListandoEventos(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    list_display_links = ("id", "name")

admin.site.register(Event, ListandoEventos)