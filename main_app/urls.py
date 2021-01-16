from django.urls import path
from . import views

urlpatterns = [
    path("", views.root),
    path("index", views.index),
    path("destroy_session", views.reset),
]