from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

def home_view(request):
    return render(request, 'main/home.html')

def city_view(request):
    return render(request, 'main/city.html')

def riyadh_view(request):
    return render(request, 'main/riyadh.html')

def abha_view(request):
    return render(request, 'main/abha.html')

def mekkah_view(request):
    return render(request, 'main/mekkah.html')

def alula_view(request):
    return render(request, 'main/alula.html')