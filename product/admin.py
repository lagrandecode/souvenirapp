from django.contrib import admin
from .models import Product

# Register your models here.
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['category','name','product_image','price']
# admin.site.register(Product,ProductAdmin)

admin.site.register(Product)