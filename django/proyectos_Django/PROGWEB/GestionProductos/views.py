from django.shortcuts import render
from GestionProductos.models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from GestionProductos.forms import FormularioContacto
# Create your views here.
def buscar (request):
    return render(request,"busqueda/search.html")
def search (request):
    if request.GET["prd"]:
        #mensaje="Lo Encontre-- %s"%request.GET["prd"]
        productos=request.GET["prd"]
        if len(productos)>20:
            return HttpResponse("Muy largo")
        else:
            Articulo=producto.objects.filter(nombre__icontains=productos)
            return render(request, "resultado.html", {"art":Articulo,"query":productos})
    else:
        mensaje="NO hay nada en la busqueda"
        return HttpResponse(mensaje)
def contacto(request):
    if request.method=="POST":
        formulario=FormularioContacto(request.POST)
        if formulario.is_valid():
            inf=formulario.cleaned_data
            send_mail(inf['asunto'],inf['mensaje'],inf.get('email',''),['luis.vara.vega@gmail.com'])
            return render(request,"gracias.html")
    else:
        formulario= FormularioContacto()
    return render(request, "formularioC.html",{"form":formulario})