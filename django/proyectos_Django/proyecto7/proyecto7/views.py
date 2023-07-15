from django.http import HttpResponse
from django.template import loader
def condicion (request):
    lit=["A-B-C-D-E-F-G","H-I-J-K-L-M-N"]
    Dic={"lista":lit,"contra":int(1234)}
    #cargador brusco
    '''
    html=open("/home/francis/Documentos/django/proyectos_Django/proyecto7/proyecto7/doc.html")
    Tmpl=Template(html.read())--No es igual a doc
    html.close()
    contexto=Context(Dic)--Este template no necesita de un contexto
    html=Tmpl.render(contexto)
    '''
    #cargador simple y optimo
    doc=loader.get_template('doc.html')
    documento=doc.render(Dic)
    return HttpResponse(documento)
