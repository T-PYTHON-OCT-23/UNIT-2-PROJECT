
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.

def home_view (request:HttpRequest):

    #getting the cookies
    print(request.COOKIES["mode"])


    return render (request,"main/home.html")

def Riyadh_view(request: HttpRequest):

    return render(request, "main/Riyadh.html")


def Mekkah_view(request: HttpRequest):

    return render(request, "main/Mekkah.html")

def Alula_view(request: HttpRequest):

    return render(request, "main/Alula.html")

def Abha_view(request: HttpRequest):

    return render(request, "main/Abha.html")


def dark_mode_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("mode", "dark")

    return response


def light_mode_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("mode", "light")

    return response