from django.urls import path
from . import views
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('arar/', views.arar, name='arar'),
    path('riyadh/', views.riyadh, name='riyadh'),
    path('jouf/', views.jouf, name='jouf'),
    path('index/', views.index, name='index'),
    path('bot/', views.bootss, name='bootss'),
    path('Mekkah/', views.Mekkah, name='Mekkah'),
    path('Abha/', views.Abha, name='Abha'),
    path('AlUla/', views.AlUla, name='AlUla'),

]
