from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("makat/", views.makat_view, name="makat_view"),
    path("tabuk/", views.tabuk_view, name="page_tabuk_view"),
    path("riyadh/", views.riyadh_view, name="riyadh_view"),
     path("abha/", views.abha_view, name="abha_view"),
    
]