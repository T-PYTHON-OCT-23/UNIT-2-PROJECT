from django.urls import path
from . import views

app_name = "main"

urlpatterns =[
    path("" , views.home_view,name="home_view"),
    path("Riyadh/" , views.city1_view , name="city1_view"),
    path("Abha/" , views.city2_view , name="city2_view"),
    path("Jeddah/" , views.city3_view , name="city3_view"),
    path("AlUla/" , views.city4_view , name="city4_view"),
    path("subscribe/",views.subscribe,name='subscribe'),
    path("signin/",views.user_login,name="user_login"),
    path("subscribe/success/",views.success_view,name="success_view"),
    path("profile/",views.profile_view,name="profile_view"),
    path("profile/page/",views.user_view,name="user_view"),
    path("logout/page/",views.user_logout,name="user_logout"),
    

]