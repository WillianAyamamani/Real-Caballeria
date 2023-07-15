from django.shortcuts import render

def prueba (request):
    Dic={
            "Nombre":"Diego"
            }
    return render(request, "doc.html",Dic)
