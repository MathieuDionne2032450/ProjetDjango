from django.urls import path
from . import views

urlpatterns = [
    path('', views.Accueil, name='accueil'),
    path('categorie/<int:id>/', views.Fruits, name='categorie'),
    

]
