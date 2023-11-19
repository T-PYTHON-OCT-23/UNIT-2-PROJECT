from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def home(request:HttpRequest):

    return render(request,'main/home.html')

def hail_city(request:HttpRequest):

    return render(request,'main/hail.html')


def riyadh_city(request:HttpRequest):
    
    return render(request,'main/riyadh.html')


def alula_city(request:HttpRequest):

    return render(request,'main/al_ula.html')

def jeddah_city(request:HttpRequest):

    return render(request,'main/jeddah.html')

