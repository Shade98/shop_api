from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
# Create your models here.
User = get_user_model()

class Order(models.Model):
    product = models.ManyToManyField(Product,through='OrderItem')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='orders')
    total_sum = models.DecimalField( 
        max_digits=10,
        decimal_places=2,
        default=0 
    )

    statuses = {
        ('D', 'Delivered'    ),
        ('ND','Not Delivered')
    }

    status = models.CharField(max_length=2, choices=statuses)
    payment_methods = {
        ('Card', 'Card'),
        ('Cash', 'Cash')
    }

    payment = models.CharField(max_length=4,choices=payment_methods)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.pk)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product =models.ForeignKey(Product,on_delete=models.RESTRICT,related_name='order_items')
    quantity = models.PositiveSmallIntegerField(default=1)

