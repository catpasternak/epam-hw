from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("db_app page")


def categories(request):
    return HttpResponse("<h1> Something by categories<h1>")
