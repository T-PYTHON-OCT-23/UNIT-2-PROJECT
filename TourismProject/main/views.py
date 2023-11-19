from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.
def home_view(request : HttpRequest):
    
      return render(request, "main/home.html" )

def about_view(request : HttpRequest):
    
      return render(request, "main/about.html" )

def contact_view(request : HttpRequest):
    
      return render(request, "main/contact.html" )

def riyadh_view(request : HttpRequest):
    
      return render(request, "main/riyadh.html" )


def makah_view(request : HttpRequest):
    
      return render(request, "main/makah.html" )


def madina_view(request : HttpRequest):
    
      return render(request, "main/madina.html" )


def alula_view(request : HttpRequest):
    
      return render(request, "main/alula.html" )


def small_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("size", "small")

    return response


def large_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("size", "large")

    return response





