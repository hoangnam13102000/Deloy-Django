from django.urls import path
from order import views

urlpatterns = [
# ------------------------------------------ Begin Home Page -------------------------------------------------

#                           -------------------- Cart -----------------------

    path('mycart/' , views.cart, name='cart'),
    path('<int:product_id>/add_to_cart/', views.add_to_cart, name = 'add_to_cart'),
    path('clear_cart/' , views.clear_cart, name='clear_cart'),
    path('<int:product_id>/remove_from_cart/', views.remove_from_cart, name = 'remove_from_cart'),

#                           -------------------- Check Out-----------------------

    path('checkout/', views.checkout, name = 'checkout'),
    
# ------------------------------------------ End Home Page ----------------------------------------------------

# ------------------------------------------ Begin Admin Page -------------------------------------------------

#                           -------------------- COrder-----------------------

    path('order_list/', views.order_list, name = 'order_list'),
    path('<int:order_id>/delete_order/', views.delete_order, name = 'delete_order'),
    path('search_order/', views.search_order, name='search_order'),
    
# ------------------------------------------ End Admin Page ----------------------------------------------------
]