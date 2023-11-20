from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def home_view(request: HttpRequest):


    return render(request, "main/home.html")


def makat_view(request: HttpRequest):

    return render(request, "main/MakatPage.html")


def tabuk_view(request: HttpRequest):

    return render(request, "main/TabukPage.html")

def riyadh_view(request: HttpRequest):

    return render(request, "main/RiyadhPage.html")

def abha_view(request: HttpRequest):

    return render(request, "main/AbhaPage.html")




  

  

  