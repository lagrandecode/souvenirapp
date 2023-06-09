from django.contrib import admin
from .models import Orders

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','product','email','address','phone_number']
admin.site.register(Orders,OrderAdmin)
