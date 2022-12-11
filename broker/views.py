from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import FilterForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    data = {'listings': Listing.objects.filter(listing_featured_flag="Yes")}
    return render(request, "broker/index.html", data)


def about(request):
    # context = {'contacts': Contact.objects.all()}
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']

        send_mail('Contact Broker',
                  message,
                  email,
                  ['minhvuvlbay@gmail.com'],
                  fail_silently=True)
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


class FormListView(FormMixin, ListView):
    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
class PropertyListView(ListView):
    model = Listing
    template_name = 'broker/browse.html'
    context_object_name = 'listings'
    success_url = '/success/'

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('success', args=(self.object.pk,)))


def success(request):
    message = request.POST['message']
    email = request.POST['email']

    send_mail('Contact Broker',
              message,
              email,
              ['minhvuvlbay@gmail.com'],
              fail_silently=True)
    return render(request, "broker/success.html")

    # def get_queryset(self):
    #   return Listing.objects.all()
    # def post(self, request):
    #   if request.POST.get('q'):
    #      return self.get_queryset().filter(listing_city='Omaha')


class PropertyDetailView(DetailView):
    model = Listing


# class PropertyImageView(DetailView):
#    model = ListingImage


def fun(request):
    return render(request, "broker/fun.html")
