from django.contrib import admin
from product.models import *
from order.models import Order
# Register your models here.

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ProductImage)
