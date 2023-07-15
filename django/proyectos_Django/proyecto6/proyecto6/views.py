from django.http import HttpResponse
from django.template import Template,Context
import datetime
class persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    
def dinamico (request):
    ps=persona("Luis","Vara")
    date=datetime.datetime.now()
    curso={
            "nombre": ps.nombre,
            "ap":ps.apellido,
            "hora":date,
            "cursos":["EDA","PWE2","RAII","CI"]
                }
    doc=open("/home/francis/Documentos/django/proyectos_Django/proyecto6/proyecto6/doc.html")
    tpl=Template(doc.read())
    doc.close()
    ctx=Context(curso)
    doc=tpl.render(ctx)
    return HttpResponse(doc)

