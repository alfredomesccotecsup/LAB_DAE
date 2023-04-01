from django.urls import path
from .views import calcular_volumen_cilindro

urlpatterns = [
    path('', calcular_volumen_cilindro, name='calcular_volumen_cilindro'),
]
