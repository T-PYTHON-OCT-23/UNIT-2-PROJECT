from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('city/', views.city_view, name='city_view'),
    path('riyadh/', views.riyadh_view, name='riyadh_view'),
    path('abha/', views.abha_view, name='abha_view'),
    path('mekkah/', views.mekkah_view, name='mekkah_view'),
    path('alula/', views.alula_view, name='alula_view'),
]