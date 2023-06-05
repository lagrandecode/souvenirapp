from django.db import models
from sourvenirapp.authentication import User
from souvenirapp.product import Product
# Create your models here.


# class Customer(models.Models):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     pro_pics = models.ImageField(upload_to='photos/customer_photo/',null=True,blank=True)


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.EmailField(max_length=80,null=True)
    address = models.CharField(max_length=500,null=True)
    phone_number = models.CharField(max_length=14,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)

    class Meta:
        verbose_name_plural = 'Orders'


