from django.db import models
from users.models import Customer
# Create your models here.

# Table comments
class Contact(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, default=False, null=True)
    customer_name = models.CharField(max_length=200)
    customer_email= models.EmailField(max_length=20)
    content = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='contact'