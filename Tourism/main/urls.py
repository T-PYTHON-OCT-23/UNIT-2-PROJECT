from . import views
from django.urls import path

app_name = 'main'


urlpatterns = [
    path('',views.home_page_views,name='home_page_views'),
    path('rafha/', views.rafha_city_views,name='rafha_city_views'),
    path('skaka/', views.skaka_city_views,name='skaka_city_views'),
    path('arar/',views.arar_city_views,name='arar_city_views'),
    path('tabuk/',views.tabuk_city_views,name='tabuk_city_views'),
    path('dark/mode/',views.dark_mode_views, name='dark_mode_views'),
    path('light/mode',views.light_mode_views,name='light_mode_views'),
]