from django.shortcuts import render ,redirect
from django.http import HttpRequest , HttpResponse

# Create your views here.

def home_page_view(request:HttpRequest):

    return render(request,"main/home.html")

def about_page_view(request:HttpRequest):

    return render(request,"main/about.html")


def services_page_view(request:HttpRequest):

    return render(request,"main/service.html")



def cities_page_view(request:HttpRequest):

    return render(request,"main/city.html")


def contact_page_view(request:HttpRequest):

    return render(request,"main/contact.html")

def riyadh_city_page_view(request:HttpRequest):

    return render(request,"main/riyadh.html")

def abha_city_page_view(request:HttpRequest):

    return render(request,"main/abha.html")

def mekkah_city_page_view(request:HttpRequest):

    return render(request,"main/mekkah.html")

def alula_city_page_view(request:HttpRequest):

    return render(request,"main/alula.html")

def small_font_size_view(request: HttpRequest):

    response = redirect("main:about_page_view")
    response.set_cookie(key="font", value="small")

    return response

def large_font_size_view(request: HttpRequest):

    response = redirect("main:about_page_view")
    response.set_cookie(key="font", value="large")

    return response

