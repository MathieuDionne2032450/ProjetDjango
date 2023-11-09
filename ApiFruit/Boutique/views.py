from django.shortcuts import render
from django.template import loader
from . import models
from django.http import HttpResponse


# Create your views here.
def Accueil(request):
    categories = models.Categorie.objects.all()
    produits = models.Produit.objects.filter(promotion__isnull=False)
    rabais = models.Promotion.objects.all()
    
    context = {
        'rabais':rabais,
        'categories':categories,
        'produits':produits
    }

    return render(request,'accueil.html',context)


def Fruits(request,id_):
    
    produits = models.Produit.objects.all()
    categories = models.Categorie.objects.all()
    nomCat = models.Categorie.objects.get(id = id_).nom
    rabais = models.Promotion.objects.all()
    context = {
        'produits':produits,
        'categories':categories,
        'categorie':id_,
        'categorienom':nomCat,
        'rabais':rabais
    }

    return render(request,'fruits.html',context)

def Categories(request):

    categories = models.Categorie.objects.all()
    
    context = {
        'categories':categories
    }

    return render(request,'categories.html',context)
   

def NotreEquipe(request):
    
    
    context = {
        
    }

    return render(request,'NotreEquipe.html',context)





































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
    Standard = models.Categorie(nom="Standard",description="Tous les produits qui n'ont rien de particulier",image="img/fruits_normal_categorie.jpg")
    Standard.save()

    Exotique = models.Categorie(nom="Exotique",description="Tous les produits qui n'ont rien de particulier",image="img/exotique.jpeg")
    Exotique.save()

    Local = models.Categorie(nom="Local",description="Tous les produits qui n'ont rien de particulier",image="img/local.jpg")
    Local.save()

    Surgelé = models.Categorie(nom="Surgelé",description="Tous les produits qui n'ont rien de particulier",image="img/surgelé.jpg")
    Surgelé.save()

    Bio = models.Categorie(nom="Bio",description="Produit Bio et qui gouttent la terre!",image="img/bio.jpg")
    Bio.save()


    



    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------                      Produits                      --------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#


    prod1 = models.Produit(nom_produit="Pomme Honey Crisp",description_produit="1 fruit",prixBase=2.99,quantite_stock=28, poids=200,categorie=Standard)
    prod1.save()
    prodimage1 = models.ProduitImage(name="pomme",le_produit=prod1,image="img/pomme.png",ordre=0)
    prodimage1.save()

    prod2 = models.Produit(nom_produit="Poire Barlett",description_produit="1 fruit",prixBase=2.99,quantite_stock=31, poids=200,categorie=Standard)
    prod2.save()
    prodimage1 = models.ProduitImage(name="poire",le_produit=prod2,image="img/poire.png",ordre=0)
    prodimage1.save()

    prod3 = models.Produit(nom_produit="Ananas doré",description_produit="1 fruit",prixBase=6.99,quantite_stock=50, poids=500,categorie=Standard)
    prod3.save()
    prodimage1 = models.ProduitImage(name="ananas",le_produit=prod3,image="img/ananas.jpg",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Avocat hass de l'ouest",description_produit="1 fruit",prixBase=2.49,quantite_stock=30, poids=150,categorie=Standard)
    prod4.save()
    prodimage1 = models.ProduitImage(name="avocados",le_produit=prod4,image="img/avocados.jpg",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Bananes niveau 4",description_produit="1 fruit",prixBase=0.64,quantite_stock=78, poids=280,categorie=Standard)
    prod4.save()
    prodimage1 = models.ProduitImage(name="banane",le_produit=prod4,image="img/banane.jpg",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Bananes équitable et biologique",description_produit="1 fruit",prixBase=0.67,quantite_stock=78, poids=190,categorie=Bio)
    prod4.save()
    prodimage1 = models.ProduitImage(name="bananebio",le_produit=prod4,image="img/bananebio.jpg",ordre=0)
    prodimage1.save()
    prod4 = models.Produit(nom_produit="Cerise Douce Bio",description_produit="1 sac de fruits",prixBase=11.99,quantite_stock=25, poids=540,categorie=Bio)
    prod4.save()
    prodimage1 = models.ProduitImage(name="cherry",le_produit=prod4,image="img/cherry.png",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Citron gros",description_produit="1 fruit",prixBase=1.29,quantite_stock=56, poids=120,categorie=Standard)
    prod4.save()
    prodimage1 = models.ProduitImage(name="citron",le_produit=prod4,image="img/citron.png",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Fruit du Dragon",description_produit="1 fruit",prixBase=3.99,quantite_stock=59, poids=220,categorie=Exotique)
    prod4.save()
    prodimage1 = models.ProduitImage(name="Dragon_Fruit",le_produit=prod4,image="img/Dragon_Fruit.png",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Figue fraiche brune",description_produit="1 fruit",prixBase=2.99,quantite_stock=59, poids=220,categorie=Exotique)
    prod4.save()
    prodimage1 = models.ProduitImage(name="figue",le_produit=prod4,image="img/figue.png",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Fraises",description_produit="1 panier de fruit",prixBase=5.29,quantite_stock=52, poids=459,categorie=Standard)
    prod4.save()
    prodimage1 = models.ProduitImage(name="fraise",le_produit=prod4,image="img/fraise.jpg",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Kiwi doré",description_produit="1 fruit",prixBase=1.29,quantite_stock=48, poids=64,categorie=Standard)
    prod4.save()
    prodimage1 = models.ProduitImage(name="kiwi",le_produit=prod4,image="img/kiwi.png",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Lime verte petite",description_produit="1 fruit",prixBase=1.29,quantite_stock=51, poids=125,categorie=Standard)
    prod4.save()
    prodimage1 = models.ProduitImage(name="lime",le_produit=prod4,image="img/lime.png",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Grosse orange navel",description_produit="1 fruit",prixBase=2.29,quantite_stock=88, poids=335,categorie=Standard)
    prod4.save()
    prodimage1 = models.ProduitImage(name="orange",le_produit=prod4,image="img/orange.jpg",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Papaye jumbo",description_produit="1 fruit",prixBase=10.54,quantite_stock=88, poids=1600,categorie=Exotique)
    prod4.save()
    prodimage1 = models.ProduitImage(name="papaye",le_produit=prod4,image="img/papaye.jpg",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Pomme grenade",description_produit="1 fruit",prixBase=3.99,quantite_stock=88, poids=240,categorie=Exotique)
    prod4.save()
    prodimage1 = models.ProduitImage(name="pomme_grenade",le_produit=prod4,image="img/pomme_grenade.jpg",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Raisins verts sans pépins",description_produit="1 sac de fruits",prixBase=7.99,quantite_stock=88, poids=1200,categorie=Standard)
    prod4.save()
    prodimage1 = models.ProduitImage(name="raisin",le_produit=prod4,image="img/raisin.png",ordre=0)
    prodimage1.save()

    prod4 = models.Produit(nom_produit="Mini melon d'eau sans pépins",description_produit="1 fruit",prixBase=5.99,quantite_stock=72, poids=5400,categorie=Standard)
    prod4.save()
    prodimage1 = models.ProduitImage(name="watermelon",le_produit=prod4,image="img/watermelon.jpg",ordre=0)
    prodimage1.save()
    prod4 = models.Produit(nom_produit="Bleuets locaux",description_produit="1 panier de fruits",prixBase=8.99,quantite_stock=22, poids=500,categorie=Local)
    prod4.save()
    prodimage1 = models.ProduitImage(name="bleuets",le_produit=prod4,image="img/bleuets.jpg",ordre=0)
    prodimage1.save()
    prod4 = models.Produit(nom_produit="Fruits des champs surgelé",description_produit="1 sac de fruits",prixBase=5.99,quantite_stock=72, poids=5400,categorie=Surgelé)
    prod4.save()
    prodimage1 = models.ProduitImage(name="champsgelé",le_produit=prod4,image="img/champsgelé.jpg",ordre=0)
    prodimage1.save()




    categories = models.Categorie.objects.all()

    context = {
        'categories':categories,
    }

    return render(request,'accueil.html',context)