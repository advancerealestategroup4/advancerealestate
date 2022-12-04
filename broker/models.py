import uuid

from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse
# Create your models here.


class Contact(models.Model):
    broker_name = models.CharField(max_length=50, blank=True, null=True)
    broker_email = models.EmailField(max_length=254, blank=True, null=True)
    broker_phone = models.CharField(max_length=12, blank=True, null=True)
    broker_image = models.ImageField(upload_to='broker_pic')
    broker_address = models.CharField(max_length=50, blank=True, null=True)
    broker_website = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.broker_name)


class Zipcode(models.Model):
    zipcode_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    zipcode_value = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.zipcode_value


class Neighborhood(models.Model):
    neighborhood_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    neighborhood_value = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.neighborhood_value


class HomeType(models.Model):
    type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_value = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.type_value


class PriceRange(models.Model):
    range_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    range_value = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.range_value


class Listing(models.Model):

    #Zipcode.objects.get()
    #Neighborhood.objects.get()
    #HomeType.objects.get()
    #PriceRange.objects.get()

    listing_id = models.CharField(max_length=50, blank=True)
    listing_number = models.IntegerField(blank=True)
    listing_street = models.CharField(max_length=50, blank=True)
    listing_city = models.CharField(max_length=50, blank=True)
    listing_state = models.CharField(max_length=2, blank=True)
    listing_zipcode = Zipcode.zipcode_value
    listing_neighborhood = Neighborhood.neighborhood_value
    listing_type = HomeType.type_value
    listing_range = PriceRange.range_value

    listing_price = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=20, blank=True)
    listing_description = models.TextField(max_length=300, blank=True)
    listing_features = models.CharField(max_length=200)

    Yes = 'Yes'
    No = 'No'
    FLAG_STATUS_CHOICES = [(Yes, 'Yes'), (No, 'No')]

    listing_featured_flag = models.CharField(max_length=3, choices=FLAG_STATUS_CHOICES, default=FLAG_STATUS_CHOICES[1], blank=True)
    listing_visible_flag = models.CharField(max_length=3, choices=FLAG_STATUS_CHOICES, default=FLAG_STATUS_CHOICES[1], blank=True)

#    listing_address = models.CharField(max_length=50)
#    listing_type = models.CharField(max_length=50)
#    listing_neighborhood = models.CharField(max_length=50)
#    listing_image1 = models.ImageField(default='default.jpg', upload_to='listing_pic')
#    listing_image2 = models.ImageField(default='default.jpg', upload_to='listing_pic')
#    listing_image3 = models.ImageField(default='default.jpg', upload_to='listing_pic')
#    listing_image4 = models.ImageField(default='default.jpg', upload_to='listing_pic')
#    listing_image5 = models.ImageField(default='default.jpg', upload_to='listing_pic')
#    listing_link1
#    listing_link2
#    listing_link3
#    listing_link4

    Available = 'Available'
    Pending = 'Pending'
    Sold = 'Sold'
    LISTING_STATUS_CHOICES = [(Available, 'Available'), (Pending, 'Pending'), (Sold, 'Sold')]
    listing_availability = models.CharField(max_length=9, choices=LISTING_STATUS_CHOICES, default=LISTING_STATUS_CHOICES[0])

    def get_absolute_url(self):
        return reverse('details', args=[str(self.listing_id)])

    def __str__(self):
        return str(self.listing_id)


class ListingImages(models.Model):
    #Listing.objects.get()

    listing_id = Listing.listing_id
    listing_image1 = models.ImageField(default='default.jpg', upload_to='listing_pic', blank=True)
    listing_image2 = models.ImageField(default='default.jpg', upload_to='listing_pic', blank=True)
    listing_image3 = models.ImageField(default='default.jpg', upload_to='listing_pic', blank=True)
    listing_image4 = models.ImageField(default='default.jpg', upload_to='listing_pic', blank=True)
    listing_image5 = models.ImageField(default='default.jpg', upload_to='listing_pic', blank=True)
