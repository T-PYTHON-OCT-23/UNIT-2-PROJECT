from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("riyadh/", views.riyadh, name="riyadh"),
    path("jeddah/", views.jeddah, name="jeddah"),
    path("makkah/", views.makkah, name="makkah"),
    path("alula/", views.alula, name="alula"),
]
