from django.urls import path
from quoteApp import views

urlpatterns = [
    path("quote/", views.displayQuote),
]
