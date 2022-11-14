from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    return render(request, "broker/index.html")


def about(request):
    context = {'contacts': Contact.objects.all()}
    return render(request, "broker/about.html", context)


def browse(request):
    return render(request, "broker/browse.html")


def fun(request):
    return render(request, "broker/fun.html")

