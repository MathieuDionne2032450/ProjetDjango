from django.urls import path
from . import views

urlpatterns = [
    path('', views.Accueil, name='accueil'),
    path('fruits/', views.Fruits, name='recherche'),
    path('categorie/<int:id_>/<int:filtre_>', views.Fruits, name='categorie'),
    path('categories/', views.Categories, name='categories'),
    path('peupler/', views.Peupler, name='peupler'),
    path('notreequipe/', views.NotreEquipe, name='NotreEquipe'),
    path('fruit/<int:id_>/', views.Fruit, name='fruit'),
    path('NousJoindre/',views.SendEmail,name='NousJoindre'),
    path('panier/<int:id_produit>/',views.PanierNouveauProduit,name='panier'),
    path('panier/',views.Panier,name='panier'),
    path('create/',views.Create,name='create'),
    path('inscription/',views.AddUserView.as_view(template_name='subscribe.html'),name="inscription")
]
