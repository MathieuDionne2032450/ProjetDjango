from django.shortcuts import render
from django.template import loader

# Create your views here.
def Accueil(request):
 
    return render(request,'accueil.html')