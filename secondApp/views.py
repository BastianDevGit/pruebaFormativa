from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vistaUnoAppDos(request):
    return HttpResponse("<h1>Hola mundo desde la app 2</h1>")

def vistaDosAppDos(request):
    return HttpResponse("<h1>Hola mundo desde la app 2 vista 2</h1>")