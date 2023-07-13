from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tag/<str:tag_name>", views.tag_name, name="tag_name"),
]
