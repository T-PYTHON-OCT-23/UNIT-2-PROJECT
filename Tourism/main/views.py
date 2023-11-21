from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse 

# Create your views here.
def home(request : HttpRequest):
  
  return render(request, "main/home.html")


def abha(request : HttpRequest):
  
  return render(request, "main/abha.html")
 

def amlg(request : HttpRequest):
  
  return render(request, "main/amlg.html")


def riyadh(request : HttpRequest):
  
  return render(request, "main/riyadh.html")


def alula(request : HttpRequest):
  
  return render(request, "main/alula.html")

