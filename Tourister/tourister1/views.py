from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def homePage(request : HttpRequest):

    return render(request ,"tourister1/homePage.html")

def contactPage(request : HttpRequest):

    return render(request ,"tourister1/contact.html")



def riyadh(request : HttpRequest):

    return render(request ,"tourister1/riyadh.html")

def jeddah(request : HttpRequest):

    return render(request ,"tourister1/jeddah.html")

def alula(request : HttpRequest):

    return render(request ,"tourister1/alula.html")

def abha(request : HttpRequest):

    return render(request ,"tourister1/abha.html")

def aboutUs(request : HttpRequest):

    return render(request ,"tourister1/aboutUs.html")