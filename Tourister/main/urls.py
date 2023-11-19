from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('' ,views.home ,name="home"),
    path('hail/city/',views.hail_city,name='hail'),
    path('riyadh/city',views.riyadh_city,name='riyadh'),
    path('alual/city/',views.alula_city,name="al_ula"),
    path("jeddah",views.jeddah_city,name="jeddah")
]
