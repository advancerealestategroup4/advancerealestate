from django.contrib import admin

# Register your models here.
from .models import Contact
from .models import Listing

admin.site.register(Contact)
admin.site.register(Listing)