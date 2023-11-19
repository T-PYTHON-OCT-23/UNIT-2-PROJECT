from django.urls import path
from . import views

app_name = "Tourism_main"


urlpatterns = [
    path("",views.home_views, name="home_views"),
    path("city/Riyadh/",views.Riyadh_views,name="Riyadh_views"),
    path("city/Jazan/", views.Jazan_views, name="Jazan_views"),
    path("city/mekkah/",views.Mekkah_views, name="Mekkah_views"),
    path("city/Alula/", views.Alula_views, name="Alula_views"),
    path("sigin/", views.Sigin_views, name="Sigin_views")
]
