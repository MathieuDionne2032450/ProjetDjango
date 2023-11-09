from django.urls import path
from . import views

urlpatterns = [
    path('', views.Accueil, name='accueil'),
    path('categorie/<int:id_>/', views.Fruits, name='categorie'),
    path('categories/', views.Categories, name='categories'),
    path('peupler/', views.Peupler, name='peupler'),
    path('NotreEquipe/', views.NotreEquipe, name='NotreEquipe'),
    

]
