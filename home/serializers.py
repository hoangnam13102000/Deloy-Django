from rest_framework import serializers
from . models import Contact

class  ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contact
        fields = (
            'id','username','customer_name','customer_email','content','date_added'
        )
