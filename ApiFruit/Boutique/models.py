from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


#Classe Catégorie
class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom_produit = models.CharField(max_length=255,null=False)
    quantite_stock = models.IntegerField(validators=[MinValueValidator(0,"La quantite doit etre superrieur a 0")], default=0, null=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,null=True)
    description_produit = models.CharField(max_length=255,null=True)
    poids = models.FloatField(validators=[MinValueValidator(0,"Le poid doit etre superrieur a 0")], default=0, null=False)
    prix = models.FloatField(validators=[MinValueValidator(0,"Le prix doit etre superrieur a 0")],null=False, default=0)
    def __str__(self):
        return self.nom_produit
    
class ProduitImg (models.Model):
    id_produit = models.IntegerField(validators=[MinValueValidator(0,"L'id doit etre superieur a 0")], null=False)
    path = models.CharField(max_length=255, null=True)

class Promotion(models.Model):
    type_rabais = models.CharField(max_length=255,null=False)
    valeur = models.IntegerField(validators=[MinValueValidator(0,"La valeur doit etre superieur a 0")],null=False)
    description_promotion = models.CharField(max_length=255,null=True)
    produit_touche = models.ManyToManyField(Produit)
    def nombre_produit_promu(self):
        return self.produit_touche.count()
    def __str__(self):
        return self.description_promotion

class Commande(models.Model):
    #determine si la commande est dans le panier ou si elle est paye et en cours de livraison
    commander = models.BooleanField(default=False)
    date_commander = models.DateTimeField(null=True)
    id_client = models.IntegerField(validators=[MinValueValidator(0,"L'id doit etre superrieur a 0")],null=False)
    
class Client(models.Model):
    nom_client = models.CharField(max_length=255,null=False)
    prenom_client = models.CharField(max_length=255,null=False)
    mot_de_passe = models.CharField(max_length=255,null=False)
    adresse = models.CharField(max_length=255,null=False)
    courriel = models.CharField(max_length=255,null=False)
    num_telephone = models.CharField(max_length=255,null=True)
    date_inscription = models.DateTimeField()
    def __str__(self):
        return self.prenom_client + " " + self.nom_client