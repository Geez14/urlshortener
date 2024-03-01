from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create", views.create, name="create"),
    path("<str:pk>", views.go, name="go"),
    path("create/api_key=<str:key>", views.api_create, name="api_create")
]
