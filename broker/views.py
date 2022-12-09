from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
from .forms import FilterForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    data = {'listings': Listing.objects.filter(listing_featured_flag="Yes")}
    return render(request, "broker/index.html", data)


def about(request):
    #context = {'contacts': Contact.objects.all()}
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']

        send_mail('Contact Broker',
                   message,
                  email,
                   ['minhvuvlbay@gmail.com'],
                   fail_silently= True)
        return render(request, "broker/success.html")
    return render(request, "broker/about.html")


# def browse(request):
#     form = FilterForm()
#     listings = []
#     if request.POST:
#         form = FilterForm(request.POST)
#         if form.is_valid():
#            # selectedlisting = form.cleaned_data['selectedlisting']
#             #if selectedlisting == None:
#             new_listings = list(Listing.objects.all())
#             output = []
#             for listing in new_listings:
#                 if listing.listing_city == 'Omaha':
#                     output.append(listing)
#             print(output)
#             # else:
#             #    listings = Listing.objects.filter(listing_zipcode=68123)
#             context = {'listing': output, 'form': form}
#             return render(request, 'broker/browse.html', context)



class PropertyListView(ListView):
    model = Listing
    template_name = 'broker/browse.html'
    context_object_name = 'listings'

    #def get_queryset(self):
     #   return Listing.objects.all()
    #def post(self, request):
     #   if request.POST.get('q'):
      #      return self.get_queryset().filter(listing_city='Omaha')

class PropertyDetailView(DetailView):
    model = Listing


# class PropertyImageView(DetailView):
#    model = ListingImage


def fun(request):
    return render(request, "broker/fun.html")




