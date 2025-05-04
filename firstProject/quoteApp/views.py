from django.shortcuts import render
from django.http import HttpResponse


def displayQuote(req):
    return HttpResponse("<h3>Best Investment is to practice code</h3>")
