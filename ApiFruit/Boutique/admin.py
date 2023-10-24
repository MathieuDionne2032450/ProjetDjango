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
    list_display = ['nom_produit','description_produit','id_categorie','quantite_stock','prix']
    ordering = ['nom_produit']
    search_fields = ['nom_produit']


