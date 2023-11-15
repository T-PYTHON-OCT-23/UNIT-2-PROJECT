from django.urls import path
from . import views
app_name = "tourister1"

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("contact/", views.contactPage, name="contactPage"),
    path("home/", views.homePage, name="home"),
]