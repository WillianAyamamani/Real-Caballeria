from django.shortcuts import render
def messi(request):
    return render(request,"blog.html",{"nombre":"Ronaldo"})
def inicio (request):
    return render(request,"doc.html")
def fifa (request):
    return render(request,"text.html")
