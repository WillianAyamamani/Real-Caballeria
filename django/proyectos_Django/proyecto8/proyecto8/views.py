#simplificacion
'''
from django.http import HttpResponse
from django.template import loader
'''
from django.shortcuts import render
def prueba(request):
    Dic={"Valor":[1,2,3,4,5],"contra":int(1234)}
    #valor general
    '''
    doc=loader.get_template("doc.html")
    documento=doc.render(Dic)
    '''
    #simplificacion
    return render(request, "doc.html", Dic)

