from django.shortcuts import render , redirect 
from django.http import HttpRequest , HttpResponse


# Create your views here.
def home_view(request : HttpRequest):
    return render (request , 'main/home.html')


def contact_view (request:HttpRequest):
    return render (request , 'main/contact.html')

def riyadh_view (request:HttpRequest):
    return render (request , 'main/riyadh.html')

def makka_view (request:HttpRequest):
    return render (request , 'main/makka.html')


def abha_view (request:HttpRequest):
    return render (request , 'main/abha.html')

def farasan_view(request:HttpRequest):
    return render(request , "main/farasan.html")


def khobar_view(request:HttpRequest):
    return render(request , "main/khobar.html")


def dammam_view(request:HttpRequest):
    return render(request , "main/dammam.html")

def dark_mode(request : HttpRequest):
    response = redirect ("main:home_view")
    response.set_cookie("mode" , "dark")
    return response


def light_mode(request : HttpRequest):
    response = redirect ("main:home_view")
    response.set_cookie("mode" , "light")
    return response