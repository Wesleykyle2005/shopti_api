from django.contrib.auth.models import AbstractUser
from django.db import models

class Location(models.Model):
    """Represents a geographical location."""
    location_id = models.AutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class Media(models.Model):
    """Represents a media file, such as an image or video."""
    media_id = models.AutoField(primary_key=True)
    url = models.URLField()
    type = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(null=True, blank=True)

class User(AbstractUser):
    """Custom user model that extends Django's AbstractUser."""
    user_type = models.CharField(max_length=50, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)

class Address(models.Model):
    """Represents a physical address associated with a user or a store."""
    address_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    store = models.ForeignKey('stores.Store', on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    municipality = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, default="Nicaragua")
    exact_address = models.TextField(max_length=500, null=True, blank=True )

