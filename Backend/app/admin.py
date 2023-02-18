from django.contrib import admin
from app.models import *

# Register your models here.
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display=('matricula','marca','modelo','capacidad')

@admin.register(Paradero)
class ParaderoAdmin(admin.ModelAdmin):
    list_display=('latitud','longitud','nombre')

@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display=('bus','paradero','hora')
    list_filter=('bus','paradero','hora')

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display=('horario',)