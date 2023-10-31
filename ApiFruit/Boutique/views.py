from django.shortcuts import render
from django.template import loader
from . import models
from django.http import HttpResponse

# Create your views here.
def Accueil(request):
    categories = models.Categorie.objects.all()

    context = {
        'categories':categories,
    }

    return render(request,'accueil.html',context)


def Fruits(request,id):
    
    produits = models.Produit.objects.all()
    categories = models.Categorie.objects.all()
    
    context = {
        'produits':produits,
        'categories':categories,
        'categorie':id
    }

    return render(request,'fruits.html',context)

def Categories(request):

    categories = models.Categorie.objects.all()
    
    context = {
        'categories':categories
    }

    return render(request,'categories.html',context)
   







































def Peupler(request):


    
    produits = models.Produit.objects.all()
    for p in produits:
        p.delete()

    categories = models.Categorie.objects.all()
    for c in categories:
        c.delete()

    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------                     CATÉGORIES                     --------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
    Standard = models.Categorie(nom="Standard",description="Tous les produits qui n'ont rien de particulier",image="fruits_normal_categorie.jpg")
    Standard.save()

    Exotique = models.Categorie(nom="Exotique",description="Tous les produits qui n'ont rien de particulier",image="fruits_normal_categorie.jpg")
    Exotique.save()

    Local = models.Categorie(nom="Local",description="Tous les produits qui n'ont rien de particulier",image="fruits_normal_categorie.jpg")
    Local.save()

    Surgelé = models.Categorie(nom="Surgelé",description="Tous les produits qui n'ont rien de particulier",image="fruits_normal_categorie.jpg")
    Surgelé.save()

    Bio = models.Categorie(nom="Bio",description="Produit Bio et qui gouttent la terre!",image="fruits_normal_categorie.jpg")
    Bio.save()

    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------                      Produits                      --------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#


    prod1 = models.Produit(nom_produit="Pomme Honey Crisp",description_produit="1 fruit",prix=2.99,quantite_stock=28, poids=200,categorie=Standard,image="pomme.png")
    prod1.save()


    prod2 = models.Produit(nom_produit="Poire Barlett",description_produit="1 fruit",prix=2.99,quantite_stock=31, poids=200,categorie=Standard,image="poire.png")
    prod2.save()
 

    prod3 = models.Produit(nom_produit="Ananas doré",description_produit="1 fruit",prix=6.99,quantite_stock=50, poids=500,categorie=Standard,image="ananas.jpg")
    prod3.save()
 

    prod4 = models.Produit(nom_produit="Avocat hass de l'ouest",description_produit="1 fruit",prix=2.49,quantite_stock=30, poids=150,categorie=Standard,image="avocados.jpg")
    prod4.save()


    prod4 = models.Produit(nom_produit="Bananes niveau 4",description_produit="1 fruit",prix=0.64,quantite_stock=78, poids=280,categorie=Standard,image="banane.jpg")
    prod4.save()
  

    prod4 = models.Produit(nom_produit="Bananes équitable et biologique",description_produit="1 fruit",prix=0.67,quantite_stock=78, poids=190,categorie=Bio,image="bananebio.jpg")
    prod4.save()
   
    prod4 = models.Produit(nom_produit="Cerise Douce Bio",description_produit="1 sac de fruits",prix=11.99,quantite_stock=25, poids=540,categorie=Bio,image="cherry.png")
    prod4.save()
   

    prod4 = models.Produit(nom_produit="Citron gros",description_produit="1 fruit",prix=1.29,quantite_stock=56, poids=120,categorie=Standard,image="citron.png")
    prod4.save()
    

    prod4 = models.Produit(nom_produit="Fruit du Dragon",description_produit="1 fruit",prix=3.99,quantite_stock=59, poids=220,categorie=Exotique,image="Dragon_Fruit.png")
    prod4.save()
    

    prod4 = models.Produit(nom_produit="Figue fraiche brune",description_produit="1 fruit",prix=2.99,quantite_stock=59, poids=220,categorie=Exotique,image="figue.png")
    prod4.save()
    

    prod4 = models.Produit(nom_produit="Fraises",description_produit="1 panier de fruit",prix=5.29,quantite_stock=52, poids=459,categorie=Standard,image="fraise.jpg")
    prod4.save()
    

    prod4 = models.Produit(nom_produit="Kiwi doré",description_produit="1 fruit",prix=1.29,quantite_stock=48, poids=64,categorie=Standard,image="kiwi.png")
    prod4.save()
    

    prod4 = models.Produit(nom_produit="Lime verte petite",description_produit="1 fruit",prix=1.29,quantite_stock=51, poids=125,categorie=Standard,image="lime.png")
    prod4.save()
    

    prod4 = models.Produit(nom_produit="Grosse orange navel",description_produit="1 fruit",prix=2.29,quantite_stock=88, poids=335,categorie=Standard,image="orange.jpg")
    prod4.save()
    

    prod4 = models.Produit(nom_produit="Papaye jumbo",description_produit="1 fruit",prix=10.54,quantite_stock=88, poids=1600,categorie=Exotique,image="papaye.jpg")
    prod4.save()
    

    prod4 = models.Produit(nom_produit="Pomme grenade",description_produit="1 fruit",prix=3.99,quantite_stock=88, poids=240,categorie=Exotique,image="pomme_grenade.jpg")
    prod4.save()
    

    prod4 = models.Produit(nom_produit="Raisins verts sans pépins",description_produit="1 sac de fruits",prix=7.99,quantite_stock=88, poids=1200,categorie=Standard,image="raisin.png")
    prod4.save()
    

    prod4 = models.Produit(nom_produit="Mini melon d'eau sans pépins",description_produit="1 fruit",prix=5.99,quantite_stock=72, poids=5400,categorie=Standard,image="watermelon.jpg")
    prod4.save()


    categories = models.Categorie.objects.all()

    context = {
        'categories':categories,
    }

    return render(request,'accueil.html',context)