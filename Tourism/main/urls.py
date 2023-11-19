from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("Riyadh/", views.Riyadh_view, name="Riyadh_view"),
    path("Mekkah/", views.Mekkah_view, name="Mekkah_view"),
    path("Abha/", views.Abha_view, name="Abha_view"),
    path("Alula/", views.Alula_view, name="Alula_view"),
     path("mode/dark/", views.dark_mode_view, name="dark_mode_view"),
    path("mode/light/", views.light_mode_view, name="light_mode_view"),
]