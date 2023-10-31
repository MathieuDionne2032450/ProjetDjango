from django.shortcuts import render
from django.template import loader
from . import models
from django.http import HttpResponse

# Create your views here.
def Accueil(request):


    
    produits = models.Produit.objects.all()
    for p in produits:
        p.delete()

    imagesproduits = models.ProduitImg.objects.all()
    for ip in imagesproduits:
        ip.delete()

    categories = models.Categorie.objects.all()
    for c in categories:
        c.delete()

    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------                     CATÉGORIES                     --------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
    Standard = models.Categorie(nom="Standard",description="Tous les produits qui n'ont rien de particulier",image="fruits_standard_categorie.jpeg")
    Standard.save()

    Exotique = models.Categorie(nom="Exotique",description="Tous les produits qui n'ont rien de particulier",image="fruits_exotique_categorie.jpeg")
    Exotique.save()

    Local = models.Categorie(nom="Local",description="Tous les produits qui n'ont rien de particulier",image="fruits_local_categorie.jpeg")
    Local.save()

    Surgelé = models.Categorie(nom="Surgelé",description="Tous les produits qui n'ont rien de particulier",image="fruits_surgele_categorie.jpeg")
    Surgelé.save()

    Bio = models.Categorie(nom="Bio",description="Produit Bio et qui gouttent la terre!",image="fruits_bio_categorie.jpeg")
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
   

    

    prod4 = models.Produit(nom_produit="Mini melon d'eau sans pépins",description_produit="1 fruit",prix=5.99,quantite_stock=72, poids=5400,categorie=Standard,image="watermelon.jpg")
    prod4.save()
    






    produits = models.Produit.objects.all()
    imgs = models.ProduitImg.objects.all()
    categories = models.Categorie.objects.all()

    context = {
        'produits':produits,
        'imgs':imgs,
        'categories':categories
    }

    return render(request,'accueil.html',context)



   