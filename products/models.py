from django.db import models

class Category(models.Model):
    """Represents a category for products."""
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=20)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

class Product(models.Model):
    """Represents a product offered by a store."""
    product_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    media = models.ForeignKey('users.Media', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

class ProductCategory(models.Model):
    """Intermediate model to link products to categories."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class ProductSubcategories(models.Model):
    """Intermediate model to link products to subcategories."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)

class ProductVariation(models.Model):
    """Represents a variation of a product, such as size or color."""
    variation_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute_type = models.CharField(max_length=50)
    value = models.CharField(max_length=100)
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_units = models.IntegerField(default=0)
    media = models.ForeignKey('users.Media', on_delete=models.SET_NULL, null=True)

class Discount(models.Model):
    """Represents a discount for a product or a store."""
    discount_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    store = models.ForeignKey('stores.Store', on_delete=models.SET_NULL, null=True, blank=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

# Create your models here.
