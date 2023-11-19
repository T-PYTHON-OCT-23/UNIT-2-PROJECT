from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_page(request : HttpRequest):
    return render(request,"main/home.html")

def riyadh_page_view(request : HttpRequest):
    return render(request,"main/riyadh.html")

def jeddah_page_view(request : HttpRequest):
    return render(request,"main/jeddah.html")

def makkah_page_view(request : HttpRequest):
    return render(request,"main/makkah.html")

def alula_page_view(request : HttpRequest):
    return render(request,"main/alula.html")

def about_us_page(request : HttpRequest):
    return render(request , "main/about_us.html")