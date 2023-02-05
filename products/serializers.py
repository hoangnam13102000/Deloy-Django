from rest_framework import serializers
from . models import Product,Category,Comment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= ('id','image', 'title', 'category', 'price', 'description','is_active','brand')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields= ('id','name')
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=('id','product','commenter_name','commenter_email','comment_body','date_added')
        