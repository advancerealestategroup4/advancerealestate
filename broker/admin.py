from django.contrib import admin

# Register your models here.
from .models import Contact
from .models import Listing
from .models import Zipcode
from .models import Neighborhood
from .models import HomeType
from .models import PriceRange
from .models import ListingImage

admin.site.register(Contact)
admin.site.register(Listing)
admin.site.register(Zipcode)
admin.site.register(Neighborhood)
admin.site.register(HomeType)
admin.site.register(PriceRange)
admin.site.register(ListingImage)
