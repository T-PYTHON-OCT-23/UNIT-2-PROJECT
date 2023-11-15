from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def homePage(request : HttpRequest):

    return render(request ,"tourister1/homePage.html")

def contactPage(request : HttpRequest):

    return render(request ,"tourister1/contact.html")

def home(request : HttpRequest):

    return render(request ,"tourister1/home.html")