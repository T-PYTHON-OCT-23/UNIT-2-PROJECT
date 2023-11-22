from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("",views.home_page_view,name="home_page_view"),
    path("about/",views.about_page_view,name="about_page_view"),
    path("services/",views.services_page_view,name="services_page_view"),
    path("cities/",views.cities_page_view,name="cities_page_view"),
    path("contact/",views.contact_page_view,name="contact_page_view"),
    path("riyadh/",views.riyadh_city_page_view,name="riyadh_city_page_view"),
    path("abha/",views.abha_city_page_view,name="abha_city_page_view"),
    path("mekkah/",views.mekkah_city_page_view,name="mekkah_city_page_view"),
    path("alula/",views.alula_city_page_view,name="alula_city_page_view"),
    path("font/small/", views.small_font_size_view, name="small_font_size_view"),
    path("font/large/",views.large_font_size_view ,name="large_font_size_view"),
    path("event/", views.event_view,name="event_view"),
    path("tourism/guidance/",views.tourism_guidance_view,name="tourism_guidance_view"),
    path("travel/",views.travel_view,name="travel_view")
]