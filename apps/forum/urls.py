from django.urls import path
from . import views

urlpatterns = [
    path("forum", views.forum, name="forum"),
    path("adicionar_topico", views.adicionar_topico, name="adicionar_topico"),
]
