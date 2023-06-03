from django.db import models
# from django.contrib.auth.models import User

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)


class Product(models.Model):
    CATEGORY = (
        ('Home & Garden','Home & Garden'),
        ('Clothing','Clothing'),
        ('Accessories','Accessories'),
        ('Electronics','Electronics'),
        ('Shoes','Shoes'),
        ('Jewelries','Jewelries')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    product_image = models.ImageField(upload_to='photos/product_image/',blank=True,null=True)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'