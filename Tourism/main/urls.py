from django.urls import path 
from . import views

app_name  = "main"

urlpatterns = [
    path('', views.home,name="home"),
    path('abha/',views.abha, name="abha"),
    path('amlg/',views.amlg, name="amlg"),
    path('riyadh/',views.riyadh,name="riyadh"),
    path('alula/',views.alula,name="alula"),
]
