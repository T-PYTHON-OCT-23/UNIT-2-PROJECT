from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def arar(request):
    return render(request, 'main/arar.html')

def riyadh(request):
    return render(request, 'main/riyadh.html')

def jouf(request):
    return render(request, 'main/jouf.html')

def index(request):
    return render(request, 'main/index.html')

def bootss(request):
    return render(request, 'main/bootss.html')
def Mekkah(request):
    return render(request, 'main/Mekkah.html')
def Abha(request):
    return render(request, 'main/Abha.html')
def AlUla(request):
    return render(request, 'main/AlUla.html')