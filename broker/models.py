from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse
# Create your models here.


class Contact(models.Model):
    broker_name = models.CharField(max_length=50)
    broker_email = models.EmailField(max_length=254)
    broker_phone = models.CharField(max_length=12)
    broker_image = models.ImageField(upload_to='broker_pic')

    def __str__(self):
        return str(self.broker_name)


class Listing(models.Model):
    listing_address = models.CharField(max_length=50)
    listing_price = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=20)
    listing_description = models.TextField(max_length=300)
    listing_features = models.CharField(max_length=200)
    listing_type = models.CharField(max_length=50)
    listing_neighborhood = models.CharField(max_length=50)
    listing_image1 = models.ImageField(default='default.jpg', upload_to='listing_pic')
    listing_image2 = models.ImageField(default='default.jpg', upload_to='listing_pic')
    listing_image3 = models.ImageField(default='default.jpg', upload_to='listing_pic')
    listing_image4 = models.ImageField(default='default.jpg', upload_to='listing_pic')
    listing_image5 = models.ImageField(default='default.jpg', upload_to='listing_pic')
    #listing_link1
    #listing_link2
    #listing_link3
    #listing_link4
    Available = 'Available'
    Pending = 'Pending'
    Sold = 'Sold'
    LISTING_STATUS_CHOICES = [(Available, 'Available'), (Pending, 'Pending'), (Sold, 'Sold')]
    listing_availability = models.CharField(max_length=9, choices=LISTING_STATUS_CHOICES, default=LISTING_STATUS_CHOICES[0])

    def get_absolute_url(self):
        return reverse('details', args=[self.id])

    def __str__(self):
        return str(self.listing_address)