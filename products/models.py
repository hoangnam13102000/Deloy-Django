from django.db import models

# Create your models here.

# Table Category
class Category(models.Model):
    name=models.CharField(max_length=255, db_index=True)
    class Meta:
        db_table='Category'
    def __str__(self):
        return self.name
    
# Table Product
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False, null=True)
    image=models.ImageField(upload_to='images/products',null=False, default=None)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=500)
    price=models.IntegerField(default=0)
    is_active=models.BooleanField(default=True)
    featured=models.CharField(max_length=255, default=None)
    brand=models.CharField(max_length=255,null=False, default=None)
    class Meta:
        db_table='Product'
    def __str__(self):
        return self.title

# Table comments
class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE, default=False, null=True)
    commenter_name = models.CharField(max_length=200)
    commenter_email= models.EmailField(max_length=20)
    comment_body = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='comment'