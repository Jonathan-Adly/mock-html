from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("documentation", views.documentation, name="documentation"),
    path("tag/<str:tag_name>", views.tag_name, name="tag_name"),
    path("gist/<str:gist_id>", views.github_gist, name="gist"),
]
