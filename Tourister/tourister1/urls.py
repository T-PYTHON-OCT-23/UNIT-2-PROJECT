from django.urls import path
from . import views
app_name = "tourister1"

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("contact/", views.contactPage, name="contactUs"),
    path("city/Riyadh/", views.riyadh, name="cityRiyadh"),
    path("city/Jeddah/", views.jeddah, name="cityJeddah"),
    path("city/AlUla/", views.alula, name="cityAlula"),
    path("city/Abha/", views.abha, name="cityAbha"),
    path("city/about/", views.aboutUs, name="aboutUs"),
]

