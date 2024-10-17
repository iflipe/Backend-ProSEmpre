from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("videos", views.videos, name="videos"),
    path ('pais-e-profs', views.pais_e_profs, name = 'pais-e-profs'),
]
