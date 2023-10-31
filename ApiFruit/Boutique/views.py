from django.shortcuts import render
from django.template import loader
from . import models
from django.http import HttpResponse

# Create your views here.
def Accueil(request):


    produits = models.Produit.objects.all()
    imgs = models.ProduitImg.objects.all()
    categories = models.Categorie.objects.all()

    context = {
        'produits':produits,
        'imgs':imgs,
        'categories':categories
    }

    return render(request,'accueil.html',context)



   