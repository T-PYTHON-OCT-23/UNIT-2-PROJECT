from django.urls import path
from .import views

app_name='main'

urlpatterns=[

    path("",views.home_view, name="home_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("city/Riyadh/", views.riyadh_view, name="riyadh_view"),
    path("city/Jeddah/", views.jeddah_view, name="jeddah_view"),
    path("city/Alula/", views.alula_view, name="alula_view"),
    path("city/Makkah/", views.makkah_view, name="makkah_view"),
    path("city/Dammam/", views.Dammam_view, name="Dammam_view"),
    path("mode/dark/", views.dark_mode_view, name="dark_mode_view"),
    path("mode/light/", views.light_mode_view, name="light_mode_view"),

]