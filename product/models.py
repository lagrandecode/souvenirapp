from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    HOME_EQUIPMENT = 'Home & Garden'
    CLOTHING = 'Clothing'
    ACCESSORIES = 'Accessories'
    ELECTRONICS = 'Electronics'
    SHOES = 'Shoes'
    JEWELRIES = 'Jewelries'
    CATEGORY = (
        (HOME_EQUIPMENT,'Home & Garden'),
        (CLOTHING,'Clothing'),
        (ACCESSORIES,'Accessories'),
        (ELECTRONICS,'Electronics'),
        (SHOES,'Shoes'),
        (JEWELRIES,'Jewelries')
    )
    category = models.CharField(max_length=50,choices=CATEGORY,default=HOME_EQUIPMENT)
    name = models.CharField(max_length=500)
    product_image = models.ImageField(upload_to='photos/product_image/',blank=True,null=True)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Product'
        
