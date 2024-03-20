from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('administrador/', views.administrador),
    path('registrarBarbero/', views.registroBarbero),
    path('perfilAdmin/', views.perfilAdmin)
]
