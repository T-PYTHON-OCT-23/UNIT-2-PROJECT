from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request:HttpRequest):

    return render(request, 'main/home.html')


def jeddah_view(request:HttpRequest):
    return render(request ,'main/jeddah.html')

def alula_view(request:HttpRequest):
    return render(request ,'main/alula.html')

def riyadh_view(request:HttpRequest):
    return render(request ,'main/riyadh.html')

def contact_view(request:HttpRequest):
    return render(request ,'main/contact.html')

def makkah_view(request:HttpRequest):
    return render(request ,'main/makkah.html')

def Dammam_view(request:HttpRequest):
    return render(request ,'main/Dammam.html')


def dark_mode_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("mode", "dark")

    return response


def light_mode_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("mode", "light")

    return response