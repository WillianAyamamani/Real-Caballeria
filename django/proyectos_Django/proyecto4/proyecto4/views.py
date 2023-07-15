from django.http import HttpResponse
from django.template import Template,Context
def prueba (request):
    doc_ext=open("/home/francis/Documentos/django/proyectos_Django/proyecto4/proyecto4/plantilla.html")

    plt=Template(doc_ext.read())

    doc_ext.close()

    ctx=Context()

    doc=plt.render(ctx)
    return HttpResponse(doc);
