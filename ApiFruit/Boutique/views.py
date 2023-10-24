from django.shortcuts import render
from django.template import loader
from . import models
from django.http import HttpResponse

# Create your views here.
def Accueil(request):
    produits = models.Produit.objects.all()
    for p in produits:
        p.delete()
    prod1 = models.Produit(name="Pomme Honey Crisp",Description="1 fruit (environ 200 g) ",prix=2.99,img="pomme.png")
    prod1.save()
    prod1 = models.Produit(name="Poire Barlett",Description="1 fruit (environ 200 g) ",prix=3.99,img="poire.png")
    prod1.save()

    produits = models.Produit.objects.all()

    context = {
        'produits':produits,
    }

    return render(request,'accueil.html',context)



   