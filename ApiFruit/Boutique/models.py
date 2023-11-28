from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.html import mark_safe
from django.db.models import Count
import datetime
from django.contrib.auth.models import User

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
    date_debut = models.DateField(null = True)
    date_fin = models.DateField(null = True)
    promo_valide = models.BooleanField(null=True)
    #Fonction pour que les promo s'ajuste automatiquement PAS TERMINER
    #promo_sujet = models.CharField(max_length=255)
    #select_Promo_sujet = (
     #   ('Categorie'),
      #  ('Prix'),
       # ('Description'),
    #)
    @property
    def valide(self):
        if(self.date_debut != None):
            if (self.date_debut > datetime.date.today() or self.date_fin < datetime.date.today()):
                self.promo_valide = False
                self.save()
                return False
        self.promo_valide = True
        self.save()
        return True

    def __str__(self):
        return self.description_promotion
    
    



class Produit(models.Model):
    nom_produit = models.CharField(max_length=255,null=False)
    quantite_stock = models.IntegerField(validators=[MinValueValidator(0,"La quantite doit etre superrieur a 0")], default=0, null=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT,null=True)
    description_produit = models.CharField(max_length=255,null=True)
    poids = models.FloatField(validators=[MinValueValidator(0,"Le poid doit etre superrieur a 0")], default=0, null=False)
    prixBase = models.FloatField(validators=[MinValueValidator(0,"Le prix doit etre superrieur a 0")],null=False, default=0)
    promotion = models.ForeignKey(Promotion,on_delete=models.SET_NULL,null=True,blank=True)

    @property
    def image_default(self):
        if (self.images.count() > 0):
            return self.images.order_by('ordre').first().image
        return None
    
    @property
    def image_else(self):
        if (self.images.count() > 0):
            return self.images.order_by('ordre').exclude(ordre=0)
        return None

    def image_tag(self):
        if(self.images.count() > 0):
            return mark_safe('<img src="/media/%s" alt="aucune image n\'a été sélectionner" height="40" />' % (self.image_default))
        else:
            return mark_safe('<img src="/media/img/default.jpg" alt="aucune image n\'a été sélectionner"  height="40" />')

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.nom_produit
    
    def PrixFinal(self):
        
        if (self.promotion != None and self.promotion.valide == False):
            self.promotion = None
            self.save()
            
        prixFinal = 0
        if(self.promotion != None):
            if(self.promotion.type_rabais == '%'):
                prixFinal = (self.prixBase*(100-self.promotion.valeur))/100
            if(self.promotion.type_rabais == '$'):
                prixFinal = self.prixBase - self.promotion.valeur
        else:
            prixFinal=self.prixBase

        return round(prixFinal,2)
    
        

        
class ProduitImage(models.Model):
    name = models.CharField(max_length=255)
    le_produit = models.ForeignKey(Produit,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to="img/",null=True)
    ordre = models.IntegerField(default=0,null=False,validators=[MinValueValidator(0,"Le prix doit etre superrieur a 0")])

    def image_tag(self):
        if(self.image != None):
            return mark_safe('<img src="/media/%s" alt="aucune image n\'a été sélectionner" height="40" />' % (self.image))
        else:
            return mark_safe('<img src="/media/img/default.jpg" alt="aucune image n\'a été sélectionner"  height="40" />')

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name

class Commande(models.Model):
    #determine si la commande est dans le panier ou si elle est paye et en cours de livraison
    commander = models.BooleanField(default=False)
    date_commander = models.DateTimeField(null=True)
    client = models.ForeignKey(User,on_delete=models.CASCADE,validators=[MinValueValidator(0,"L'id doit etre superrieur a 0")],null=False,default=1,related_name='CommandeClient')
    produit = models.ManyToManyField(Produit,)

    def get_products(self):
        if(self.produit.count != 0):
            return ",\n".join([produit.nom_produit for produit in self.produit.all()])
        
    def __str__(self):
        return 'Commande '+ self.id.__str__() + ' :' + self.client.__str__()
        

    
    

    