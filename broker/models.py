from django.db import models
# Create your models here.

class Contact(models.Model):
    broker_name = models.CharField(max_length=50)
    broker_email = models.EmailField(max_length=254)
    broker_phone = models.CharField(max_length=12)
    broker_image = models.ImageField()