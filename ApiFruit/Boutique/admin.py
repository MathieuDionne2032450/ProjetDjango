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
    
    list_display = ['image_tag','id','nom_produit','categorie','description_produit','quantite_stock','poids','prixBase','promotion',"PrixFinal"]
    ordering = ['nom_produit']
    search_fields = ['nom_produit']
    list_filter = ['categorie']




@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['description_promotion','type_rabais','valeur','valide']
    ordering = ['valeur']
    search_fields = ['description_promotion']
    list_filter = ['promo_valide']


@admin.register(models.Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['id','client','commander','date_commander','get_products']
    ordering = ['client']
    search_fields = ['client']

@admin.register(models.ProduitImage)
class ProduitImageAdmin(admin.ModelAdmin):
    list_display = ['image_tag','name']
    ordering = ['name']
    search_fields = ['name']

@admin.register(models.CommandeProduit)
class CommandeProduitAdmin(admin.ModelAdmin):
    list_display = ['produit_du_panier','la_commande','quantite']
    ordering = ['id']
    search_fields = ['id']


