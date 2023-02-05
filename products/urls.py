from django.urls import path
from products import views
urlpatterns = [
# ------------------------------------------ Begin Home Page -------------------------------------------------

#                           -------------------- Product -----------------------

     path('search_products/', views.search_products, name='search_products'),
     path('<int:product_id>/product_detail/', views.product_detail, name='product_detail'),

#                  -------------------- Create Menu Base on Category -----------------------  

     path('<int:category_id>/product_of_category/', views.product_of_category, name='product_of_category'),

# ------------------------------------------ End Home Page ----------------------------------------------------

# ------------------------------------------ Begin Admin Page -------------------------------------------------

#                           -------------------- Category -----------------------

     path('categories/', views.category_list, name='category_list'),
     path('addCategory/' , views.addCategory, name='addCategory'),
     path('<int:category_id>/edit_category/', views.edit_category, name='edit_category'),
     path('delete/<int:category_id>', views.delete_category, name='delete_category'),
     path('search_category/', views.search_category, name='search_category'),
     
#                           -------------------- Product -----------------------

     path('products/', views.product_list, name='product_list'),
     path('add_product/' , views.add_product, name='add_product'),
     path('<int:product_id>/edit_product/', views.edit_product, name='edit_product'),
     path('delete_product/<int:product_id>', views.delete_product, name='delete_product'),
     path('search_product_admin/', views.search_product_admin, name='search_product_admin'),
     
#                           -------------------- Comment -----------------------

     path('comment_list/', views.comment_list, name='comment_list'),
     path('<int:comment_id>/delete_comment', views.delete_comment, name='delete_comment'),
     path('search_comment/', views.search_comment, name='search_comment'),

# ------------------------------------------ End Admin Page ----------------------------------------------------
     
]