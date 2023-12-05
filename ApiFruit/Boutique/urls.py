from django.urls import path,include
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
    path('panier/',views.Panier,name='panier'),
    path('login/',views.Login,name='login'),
    path('subscribe/',views.Subscribe,name='subscribe'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('paiementreussi/',views.paiementreussi,name='paiementreussi'),
    path('paiementcancel/',views.paiementcancel,name='paiementcancel'),
    path('test/',views.paypal,name='paypal'),
    path('paypal-return',views.paypal_return,name='paypal-return'),
    path('paypal-cancel',views.paypal_cancel,name='paypal-cancel'),
]
