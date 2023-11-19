from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("/about", views.about_view, name="about_view"),
    path("/contact", views.contact_view, name="contact_view"),
    path("/riyadh", views.riyadh_view, name="riyadh_view"),
    path("/madina", views.madina_view, name="madina_view"),
    path("/makah", views.makah_view, name="makah_view"),
    path("/alula", views.alula_view, name="alula_view"),
     path("size/small/", views.small_view, name="small_view"),
     path("size/large/", views.large_view , name="large_view"),

]
