from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def home(request: HttpRequest):
    return render(request, 'main/home.html')


def contact(request: HttpRequest):
    return render(request, 'main/contact.html')


def riyadh(request: HttpRequest):
    return render(request, 'main/riyadh.html')


def jeddah(request: HttpRequest):
    return render(request, 'main/jeddah.html')


def makkah(request: HttpRequest):
    return render(request, 'main/makkah.html')


def alula(request: HttpRequest):
    return render(request, 'main/alula.html')
