from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Product(models,Model):
    name = models.CharField(max_length=500)
    product_image = models.ImageField(upload_to='photos/product_image/',blank=True,null=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'