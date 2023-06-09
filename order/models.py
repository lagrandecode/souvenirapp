from django.db import models
from authentication.models import User
from product.models import Product
# from django.contrib.auth.models import User
# Create your models here.





class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    email = models.EmailField(max_length=80,null=True)
    address = models.CharField(max_length=500,null=True)
    phone_number = models.CharField(max_length=14,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS,editable=False)

    class Meta:
        verbose_name_plural = 'Orders'





