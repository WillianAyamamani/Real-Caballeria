#GestionProductos/migrations/0001_initial.py
from django.db import models
# Clase de producto
class producto (models.Model):
    codigo=models.CharField(max_length=100,verbose_name="CODIFICACION")
    nombre=models.CharField(max_length=30, verbose_name="Name")
    origen=models.CharField(blank=True,null=True,max_length=50)
    caducacion=models.DateField("LA REAL FECHA")
    precio=models.IntegerField()

    def __str__(self):
        return self.nombre
    
#clase del pedido
class Pedidos (models.Model):
    numero=models.IntegerField()
    estado=models.BooleanField()
    fecha=models.DateField()
    producto=models.CharField(max_length=100)
    
    def __str__(self):
        return '\nNUMERO--%s ESTADO--%s FECHA--%s PRODUCTO--%s\n' %(self.numero,self.estado,self.fecha,self.producto)
    