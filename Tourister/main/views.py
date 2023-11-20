from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def index_view(request:HttpRequest):
    
    return render(request,"main/index.html") 

def riyadh_view(request:HttpRequest):
    
    return render(request,"main/riyadh.html") 

def abha_view(request:HttpRequest):
    
    return render(request,"main/abha.html") 

def mekkah_view(request:HttpRequest):
    
    return render(request,"main/mekkah.html") 

def test_view(request:HttpRequest):
    
    return render(request,"main/test.html") 