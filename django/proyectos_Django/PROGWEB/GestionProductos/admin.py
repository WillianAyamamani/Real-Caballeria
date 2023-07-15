from django.contrib import admin
#import product model's
from GestionProductos.models import producto,Pedidos

# Register your models here.
class Listado(admin.ModelAdmin):
    #list_display=("nombre","origen","precio")
    search_fields=("nombre","precio")
    list_filter=("nombre","origen")

class Pedido(admin.ModelAdmin):
    list_display=("numero","estado","producto")
    list_filter=("fecha",)
    date_hierarchy="fecha"
    
admin.site.register(producto,Listado)
admin.site.register(Pedidos,Pedido)