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
    path('produit_panier_delete/<int:id_produit>/',views.PanierDeleteProduit,name='produit_panier_delete'),
    path('panier/<int:id_produit>/',views.PanierNouveauProduit,name='panier'),
    path('panier/',views.Panier,name='panier'),
    path('ajout_quantite/<int:id_produit>/<int:quantite>',views.Ajout_quantite,name="ajout_quantite"),
    path('create/',views.Create,name='create'),
    path('inscription/',views.AddUserView.as_view(template_name='subscribe.html'),name="inscription"),
    path('edit/',views.EditUserView.as_view(),name="edit_user"),
    path('password/', views.ChangeUserPasswordView.as_view(template_name='registration/change_password.html'), name="change_password"),
    path('password-success/', views.user_password_success_view, name='change_password_success'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('paiementreussi/',views.paiementreussi,name='paiementreussi'),
    path('paiementcancel/',views.paiementcancel,name='paiementcancel'),
    path('test/',views.paypal,name='paypal'),
    path('paypal-return',views.paypal_return,name='paypal-return'),
    path('paypal-cancel',views.paypal_cancel,name='paypal-cancel'),
]
