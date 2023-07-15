from django.http import HttpResponse
from django.template import Template,Context
import datetime
class persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido


def prueba (request):
    pr=persona("Francis","Añasco")
    nombre="juan"
    apellido="messi"
    fecha=datetime.datetime.now()
    doc_ext=open("/home/francis/Documentos/django/proyectos_Django/proyecto5/proyecto5/doc.html")
    tpl=Template(doc_ext.read())
    doc_ext.close()
    ctx=Context({
        #contexto, con uso de Diccionarios
        "nombre_p":pr.nombre,
        "ape":pr.apellido,
        "hora":fecha
        })
    doc_ext=tpl.render(ctx)
    return HttpResponse(doc_ext)
