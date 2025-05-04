from django.urls import path
from templatesApp import views

urlpatterns = [
    path("template/", views.render_template),
]
