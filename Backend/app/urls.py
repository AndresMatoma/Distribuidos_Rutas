from django.urls import path
from app.views import *
urlpatterns = [
    path(r'bus/',bus),
    path(r'hora/',hora),
    path(r'ruta/',ruta),
    path(r'paradero/',paradero),
]