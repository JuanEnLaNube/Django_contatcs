from django.urls import path
from . import views
from directorio import views

urlpatterns = [
    path('', views.inicio_view, name='Inicio'),
]