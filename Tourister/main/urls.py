from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("" , views.home_view , name="home_view"),
    path("contact/" , views.contact_view , name="contact_view" ),
    path("riyadh/" , views.riyadh_view , name="riyadh_view" ),
    path("makka/" , views.makka_view , name="makka_view" ),
    path("abha/" , views.abha_view , name="abha_view" ),
    path("dark/" , views.dark_mode , name= "dark_mode"),
    path("light/" , views.light_mode , name= "light_mode"),
    path("dammam/" , views.dammam_view , name= "dammam_view"),  
    path("farasan/" , views.farasan_view , name= "farasan_view"),
    path("khobar/" , views.khobar_view , name= "khobar_view"),


]