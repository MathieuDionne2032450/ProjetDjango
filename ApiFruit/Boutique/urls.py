from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.Accueil, name='accueil'),
    

]
