from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView


def index(request):
    data = {'listings': Listing .objects.filter(listing_featured_flag="Yes")}
    return render(request, "broker/index.html", data)


def about(request):
    context = {'contacts': Contact.objects.all()}
    return render(request, "broker/about.html", context)


#def browse(request):
#    return render(request, "broker/browse.html")


class PropertyListView(ListView):
    model = Listing
    template_name = 'broker/browse.html'
    context_object_name = 'listings'


class PropertyDetailView(DetailView):
    model = Listing


#class PropertyImageView(DetailView):
#    model = ListingImage


def fun(request):
    return render(request, "broker/fun.html")
