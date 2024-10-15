from django.urls import path
from . import views

urlpatterns = [
    path("videos", views.videos, name="videos"),
    path("", views.home, name="home"),
]
