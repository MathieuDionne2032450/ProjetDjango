from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom','description','img']
    ordering = ['nom']
    search_fields = ['nom']

@admin.register(models.Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom_produit','categorie','description_produit','quantite_stock','poids','prix']
    ordering = ['nom_produit']
    search_fields = ['nom_produit']

@admin.register(models.ProduitImg)
class ProduitImgAdmin(admin.ModelAdmin):
    list_display = ['id_produit','path']
    ordering = ['id_produit']
    search_fields = ['id_produit']

@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['description_promotion','type_rabais','valeur','nombre_produit_promu']
    ordering = ['valeur']
    search_fields = ['description_promotion']

#Table de jonction les promotions avec les produits
#@admin.register(models.PromotionProduit)
#class PromotionProduitAdmin(admin.ModelAdmin):
#    list_display = ['id_promotion','id_produit']
#    ordering = ['id_promotion']
#    search_fields = ['id_promotion']


@admin.register(models.Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['id_client','commander','date_commander']
    ordering = ['id_client']
    search_fields = ['id_client']

#Table de jonction les produits avec les commande
#@admin.register(models.ProduitCommande)
#class ProduitCommandeAdmin(admin.ModelAdmin):
 #   list_display = ['id_commande','id_produit']
 #   ordering = ['id_commande']
 #   search_fields = ['id_commande']

@admin.register(models.Client)
class Client(admin.ModelAdmin):
    list_display = ['nom_client','prenom_client','mot_de_passe','adresse','courriel','num_telephone','date_inscription']
    ordering = ['nom_client']
    search_fields = ['nom_client','prenom_client']




