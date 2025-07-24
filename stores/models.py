from django.db import models

class Store(models.Model):
    """Represents a store."""
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    location = models.ForeignKey('users.Location', on_delete=models.SET_NULL, null=True)
    media = models.ForeignKey('users.Media', on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    slogan = models.CharField(max_length=255, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

class StoreMetric(models.Model):
    """Represents performance metrics for a store."""
    metric_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    metric_type = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(max_length=10)
    recorded_at = models.DateTimeField()

# Create your models here.
