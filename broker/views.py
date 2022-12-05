from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView


def index(request):
    data = {'listings': Listing .objects.filter(listing_featured_flag="Yes"), 'listing_image': ListingImage .objects.filter(listing_id=Listing.listing_id)}
    return render(request, "broker/index.html", data)


def about(request):
    context = {'contacts': Contact.objects.all()}
    return render(request, "broker/about.html", context)


# def browse(request):
    # return render(request, "broker/browse.html")


class PropertyListView(ListView):
    template_name = 'broker/browse.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return Listing.objects.order_by("listing_id")

    def get_context_data(self, **kwargs):
        context = super(PropertyListView, self).get_context_data(**kwargs)
        context.update({
            'listing_image': ListingImage.objects.order_by("listing_id")
        })
        return context


class PropertyDetailView(DetailView):
    model = Listing

    def get_context_data(self, **kwargs):
        context = super(PropertyDetailView, self).get_context_data(**kwargs)
        context['listing_image'] = ListingImage.listing_id = Listing.listing_id
        return context


class PropertyImageView(DetailView):
    model = ListingImage


def fun(request):
    return render(request, "broker/fun.html")
