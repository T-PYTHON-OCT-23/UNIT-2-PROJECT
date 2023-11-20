from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("city/Riyadh/", views.riyadh_view, name="riyadh_view"),
    path("city/Abha/", views.abha_view, name="abha_view"),
    path("city/Mekkah/", views.mekkah_view, name="mekkah_view"),
    path("test/", views.test_view, name="test_view"),

]