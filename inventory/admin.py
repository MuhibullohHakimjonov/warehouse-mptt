from django.contrib import admin
from .models import Location, Product
from mptt.admin import MPTTModelAdmin

admin.site.register(Location, MPTTModelAdmin)
admin.site.register(Product)