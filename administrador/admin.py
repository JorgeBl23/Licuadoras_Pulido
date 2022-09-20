from django.contrib import admin

from administrador.models import Elemento

# Register your models here.
@admin.register(Elemento)
class adminElemento(admin.ModelAdmin):
    list_display = ['nombre','marca','precio','foto']
    list_display_links = ['nombre']