from django.db import models

# Create your models here.

#Classe Catégorie
class Categorie(models.Model):
    nom=models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
