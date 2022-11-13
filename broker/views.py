from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    return render(request, "broker/index.html", {'title': 'Home page'})


def fun(request):
    return render(request, "broker/fun.html", {'title': 'Fun page'})

