from django.contrib import admin
from . models import Product, Comment, Category

#Register your models here.

# Product
admin.site.register(Product)
# Category
admin.site.register(Category)
# Comment
admin.site.register(Comment)
