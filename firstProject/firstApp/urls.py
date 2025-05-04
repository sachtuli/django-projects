from django.urls import path
from firstApp import views

urlpatterns = [
    path("hello/", views.display),
    path("datetime/", views.displayDateTime),
]
