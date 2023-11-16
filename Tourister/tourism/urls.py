from django.urls import path
from .views import home, city_detail
app_name='tourism'
urlpatterns = [
    path('', home, name='home'),
    path('city/<str:city_name>/', city_detail, name='city_detail'),
]
