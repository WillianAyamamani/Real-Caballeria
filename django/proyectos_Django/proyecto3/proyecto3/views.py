from django.http import HttpResponse
import datetime

def vista1 (request):#vista prueba
    documento="""<html>
    <body>
    <h1>Halland</h1>
    </body>
    </html>"""
    return HttpResponse(documento)
def fecha (request):#vista fecha
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    Fecha y Hora actual %s
    </h1>
    </body>
    </html>"""% fecha_actual
    return HttpResponse(documento)
def calculadora (request,year,edad,nombre):#parametro extra, que se manda por url
    #periodo=int(year)-2022
    periodo=year-2022
    edad_futura=edad+periodo
    documento="""
    <html>
    <body>
    <h2>
    %s
    En el año %s tendras %s años
    </h2>
    </body>
    </html>"""%(nombre,year,edad_futura)
    return HttpResponse(documento)
