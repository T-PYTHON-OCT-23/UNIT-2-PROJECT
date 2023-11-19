from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def home_page(request : HttpRequest):
    return render(request,'main/home.html')

def mecca_page(request : HttpRequest):
    return render(request,'main/mecca.html')

def riyadh_page(request : HttpRequest):
    return render(request,'main/riyadh.html')

def jeddah_page(request : HttpRequest):
    return render(request,'main/jeddah.html')

def about_page(request : HttpRequest):
    return render(request,'main/about.html')

def contact_page(request : HttpRequest):
    return render(request,'main/contact.html')

def alula_page(request : HttpRequest):
    return render(request,'main/alula.html')