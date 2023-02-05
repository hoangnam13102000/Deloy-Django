from rest_framework import serializers
from . models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields= ("id","fullname","gender","address","phone", "email","username","password")


# class CustomerCreationSerializer(serializers.Serializer):
#     fullname=serializers.CharField(max_length=100)
#     gender=serializers.CharField(max_length=20,help_text="0=Nam, 1=Nữ")
#     address=serializers.CharField(max_length=100)
#     email=serializers.EmailField(max_length=20,default="unknow@gmail.com")
#     phone=serializers.CharField(max_length=20) 
#     username=serializers.CharField(max_length=50)
#     password=serializers.CharField(max_length=50)
    
    
    