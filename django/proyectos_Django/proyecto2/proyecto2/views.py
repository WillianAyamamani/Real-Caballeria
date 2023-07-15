from django.http import HttpResponse

def saludo(request):# Primera Vista
    return HttpResponse("Viva messi")
def despedida (request):#Segunda Vista
    return HttpResponse("Barcelona")
