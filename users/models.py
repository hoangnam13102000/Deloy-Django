from django.db import models
from django.contrib.auth.models import User

# Table Customer
class Customer(models.Model):
    fullname=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=20,default="unknow@gmail.com")
    address=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=20,null=True)
    gender=models.CharField(max_length=20,null=True,help_text="0=Nam, 1=Nữ")
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table='Customer'
    def __str__(self):
        return self.username
    
# Table Employee
class Employee(models.Model):
    image=models.ImageField(upload_to='images/employees',null=False, default=None)
    fullname=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=20,default="unknow@gmail.com")
    password=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=20,null=True,help_text="0=Nam, 1=Nữ")
    phone=models.CharField(max_length=20,null=True)
    position = models.CharField(max_length=255)
    salary = models.IntegerField(default=0)
    start_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table='Employee'
    def __str__(self):
        return self.username