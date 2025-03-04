from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Location(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    location = TreeForeignKey(Location, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} ({self.type}) at {self.location}"
