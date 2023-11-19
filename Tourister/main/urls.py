from django.urls import path
from . import views
app_name = "main"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("riyadh/", views.riyadh_page_view, name="riyadh_page_view"),
    path("jeddah/", views.jeddah_page_view, name="jeddah_page_view"),
    path("makkah/", views.makkah_page_view, name="makkah_page_view"),
    path("alula/", views.alula_page_view, name="alula_page_view"),
    path("about_us/", views.about_us_page, name="about_us_page")
]