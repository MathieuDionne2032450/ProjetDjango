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
    Standard = models.Categorie(nom="Standard",description="Tous les produits qui n'ont rien de particulier",img="fruits_standard_categorie.jpeg")
    Standard.save()

    Exotique = models.Categorie(nom="Exotique",description="Tous les produits qui n'ont rien de particulier",img="fruits_exotique_categorie.jpeg")
    Exotique.save()

    Local = models.Categorie(nom="Local",description="Tous les produits qui n'ont rien de particulier",img="fruits_local_categorie.jpeg")
    Local.save()

    Surgelé = models.Categorie(nom="Surgelé",description="Tous les produits qui n'ont rien de particulier",img="fruits_surgele_categorie.jpeg")
    Surgelé.save()

    Bio = models.Categorie(nom="Bio",description="Produit Bio et qui gouttent la terre!",img="fruits_bio_categorie.jpeg")
    Bio.save()

    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------                      Produits                      --------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#


    prod1 = models.Produit(nom_produit="Pomme Honey Crisp",description_produit="1 fruit",prix=2.99,quantite_stock=28, poids=200,categorie=Standard)
    prod1.save()
    imgprod1 = models.ProduitImg(id_produit=prod1.id,path="pomme.png")
    imgprod1.save()

    prod2 = models.Produit(nom_produit="Poire Barlett",description_produit="1 fruit",prix=2.99,quantite_stock=31, poids=200,categorie=Standard)
    prod2.save()
    imgprod2 = models.ProduitImg(id_produit=prod2.id,path="poire.png")
    imgprod2.save()

    prod3 = models.Produit(nom_produit="Ananas doré",description_produit="1 fruit",prix=6.99,quantite_stock=50, poids=500,categorie=Standard)
    prod3.save()
    imgprod3 = models.ProduitImg(id_produit=prod3.id,path="ananas.jpg")
    imgprod3.save()

    prod4 = models.Produit(nom_produit="Avocat hass de l'ouest",description_produit="1 fruit",prix=2.49,quantite_stock=30, poids=150,categorie=Standard)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="avocados.jpg")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Bananes niveau 4",description_produit="1 fruit",prix=0.64,quantite_stock=78, poids=280,categorie=Standard)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="banane.jpg")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Bananes équitable et biologique",description_produit="1 fruit",prix=0.67,quantite_stock=78, poids=190,categorie=Bio)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="bananebio.jpg")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Cerise Douce Bio",description_produit="1 sac de fruits",prix=11.99,quantite_stock=25, poids=540,categorie=Bio)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="cherry.png")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Citron gros",description_produit="1 fruit",prix=1.29,quantite_stock=56, poids=120,categorie=Standard)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="citron.png")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Fruit du Dragon",description_produit="1 fruit",prix=3.99,quantite_stock=59, poids=220,categorie=Exotique)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="Dragon_Fruit.png")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Figue fraiche brune",description_produit="1 fruit",prix=2.99,quantite_stock=59, poids=220,categorie=Exotique)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="figue.png")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Fraises",description_produit="1 panier de fruit",prix=5.29,quantite_stock=52, poids=459,categorie=Standard)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="fraise.jpg")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Kiwi doré",description_produit="1 fruit",prix=1.29,quantite_stock=48, poids=64,categorie=Standard)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="kiwi.png")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Lime verte petite",description_produit="1 fruit",prix=1.29,quantite_stock=51, poids=125,categorie=Standard)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="lime.png")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Grosse orange navel",description_produit="1 fruit",prix=2.29,quantite_stock=88, poids=335,categorie=Standard)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="orange.jpg")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Papaye jumbo",description_produit="1 fruit",prix=10.54,quantite_stock=88, poids=1600,categorie=Exotique)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="papaye.jpg")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Pomme grenade",description_produit="1 fruit",prix=3.99,quantite_stock=88, poids=240,categorie=Exotique)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="pomme_grenade.jpg")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Raisins verts sans pépins",description_produit="1 sac de fruits",prix=7.99,quantite_stock=88, poids=1200,categorie=Standard)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="raisin.png")
    imgprod4.save()

    prod4 = models.Produit(nom_produit="Mini melon d'eau sans pépins",description_produit="1 fruit",prix=5.99,quantite_stock=72, poids=5400,categorie=Standard)
    prod4.save()
    imgprod4 = models.ProduitImg(id_produit=prod4.id,path="watermelon.jpg")
    imgprod4.save()






    produits = models.Produit.objects.all()
    imgs = models.ProduitImg.objects.all()
    categories = models.Categorie.objects.all()

    context = {
        'produits':produits,
        'imgs':imgs,
        'categories':categories
    }

    return render(request,'accueil.html',context)



   