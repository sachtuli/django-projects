from django.shortcuts import render
from django.http import HttpResponse
import datetime


def display(request):
    return HttpResponse("<h1> My first  Django App !!</h1>")


def displayDateTime(request):
    dt = datetime.datetime.now()
    s = f"<b> Current Date and Time: </b> {str(dt.strftime('%d/%m/%Y %H:%M:%S'))}"
    return HttpResponse(s)
