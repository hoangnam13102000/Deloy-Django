from django.db import models
from users.models import Customer,Employee
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
        ('Finished', 'Finished'),)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=False, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=False, null=True)
    customer_name= models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=255)
    total_price = models.IntegerField()
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES, default='Pending')
    def __str__(self):
        return self.customer
    class Meta:
        db_table='order'