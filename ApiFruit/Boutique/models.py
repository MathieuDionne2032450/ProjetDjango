from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.html import mark_safe

# Create your models here.

#Classe Catégorie
class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="img/",null=True)

    def __str__(self):
        return self.nom
    
    def image_tag(self):
        if(self.image != None):
            return mark_safe('<img src="/media/%s" alt="aucune image n\'a été sélectionner" height="40" />' % (self.image))
        else:
            return mark_safe('<img src="/media/img/default.jpg" alt="aucune image n\'a été sélectionner"  height="40" />')

    image_tag.short_description = 'Image'

class Promotion(models.Model):

    select_type_rabais = (('%','Pourcentage'),('$','Unitaire'))
    type_rabais = models.CharField(max_length=255,null=False,choices=select_type_rabais)
    valeur = models.IntegerField(validators=[MinValueValidator(0,"La valeur doit etre superieur a 0")],null=False)
    description_promotion = models.CharField(max_length=255,null=True)
    #Fonction pour que les promo s'ajuste automatiquement PAS TERMINER
    #promo_sujet = models.CharField(max_length=255)
    #select_Promo_sujet = (
     #   ('Categorie'),
      #  ('Prix'),
       # ('Description'),
    #)
    def __str__(self):
        return self.description_promotion
    
    



class Produit(models.Model):
    nom_produit = models.CharField(max_length=255,null=False)
    quantite_stock = models.IntegerField(validators=[MinValueValidator(0,"La quantite doit etre superrieur a 0")], default=0, null=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT,null=False,default=Categorie.objects.filter(id=1).first())
    description_produit = models.CharField(max_length=255,null=True)
    poids = models.FloatField(validators=[MinValueValidator(0,"Le poid doit etre superrieur a 0")], default=0, null=False)
    prixBase = models.FloatField(validators=[MinValueValidator(0,"Le prix doit etre superrieur a 0")],null=False, default=0)
    image = models.ImageField(upload_to="img/",null=True)
    promotion = models.ForeignKey(Promotion,on_delete=models.SET_NULL,null=True)

    def image_tag(self):
        if(self.image != None):
            return mark_safe('<img src="/media/%s" alt="aucune image n\'a été sélectionner" height="40" />' % (self.image))
        else:
            return mark_safe('<img src="/media/img/default.jpg" alt="aucune image n\'a été sélectionner"  height="40" />')

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.nom_produit
    
    def PrixFinal(self):
        prixFinal = 0
        if(self.promotion != None):
            if(self.promotion.type_rabais == '%'):
                prixFinal = (self.prixBase*(100-self.promotion.valeur))/100
            if(self.promotion.type_rabais == '$'):
                prixFinal = self.prixBase - self.promotion.valeur
        else:
            prixFinal=self.prixBase

        return prixFinal

        
class ProduitImage(models.Model):
    name = models.CharField(max_length=255)
    le_produit = models.ForeignKey(Produit,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/",null=True)
    
    def all(idProduit):
       return ProduitImage.objects.filter(id = idProduit)


class Commande(models.Model):
    #determine si la commande est dans le panier ou si elle est paye et en cours de livraison
    commander = models.BooleanField(default=False)
    date_commander = models.DateTimeField(null=True)
    id_client = models.IntegerField(validators=[MinValueValidator(0,"L'id doit etre superrieur a 0")],null=False)
    produit = models.ManyToManyField(Produit,)

    def get_products(self):
        if(self.produit.count != 0):
            return ",\n".join([produit.nom_produit for produit in self.produit.all()])

    
    
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
    