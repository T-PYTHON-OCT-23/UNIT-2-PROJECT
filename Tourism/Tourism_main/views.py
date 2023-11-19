from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_views(request:HttpRequest):

    return render(request , 'Tourism_main/home.html')

def Riyadh_views(request:HttpRequest):

    return render(request , 'Tourism_main/riyadh.html')

def Mekkah_views(request:HttpRequest):

    return render(request , 'Tourism_main/mekkah.html')

def Jazan_views(request:HttpRequest):
    
    

    return render(request , 'Tourism_main/jazan.html')

def Alula_views(request:HttpRequest):

    return render(request , 'Tourism_main/alula.html')

def Sigin_views(request:HttpRequest):

    return render(request , 'Tourism_main/Sigin.html')