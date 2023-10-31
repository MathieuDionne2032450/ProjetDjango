from django.contrib import admin
from django.utils.html import format_html
from . import models


# Register your models here.
@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom','description','image_tag']
    ordering = ['nom']
    search_fields = ['nom']

@admin.register(models.Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom_produit','categorie','description_produit','quantite_stock','poids','prix','image_tag']
    ordering = ['nom_produit']
    search_fields = ['nom_produit']




@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['description_promotion','type_rabais','valeur','nombre_produit_promu']
    ordering = ['valeur']
    search_fields = ['description_promotion']


@admin.register(models.Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['id_client','commander','date_commander','get_products']
    ordering = ['id_client']
    search_fields = ['id_client']


@admin.register(models.Client)
class Client(admin.ModelAdmin):
    list_display = ['nom_client','prenom_client','mot_de_passe','adresse','courriel','num_telephone','date_inscription']
    ordering = ['nom_client']
    search_fields = ['nom_client','prenom_client']




