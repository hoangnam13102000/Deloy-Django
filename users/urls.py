from django.urls import path
from users import views

urlpatterns = [
# ------------------------------------------ Begin Home Page -------------------------------------------------

#                           -------------------- Customer -----------------------
     path('<int:user_id>/profile_user/' , views.profile_user, name='profile_user'),
     path('<int:user_id>/edit_profile_user/' , views.edit_profile_user, name='edit_profile_user'),
     path('<int:user_id>/change_password/' , views.change_password, name='change_password'),

# ------------------------------------------ End Home Page ----------------------------------------------------

# ------------------------------------------ Begin Admin Page -------------------------------------------------

#                           -------------------- Customer -----------------------
     path('customer_list/' , views.customer_list, name='customer_list'),
     path('add_user/' , views.add_user, name='add_user'),
     path('<int:customer_id>/edit_customer_admin/' , views.edit_customer_admin, name='edit_customer_admin'),
     path('<int:customer_id>/delete_customer/' , views.delete_customer, name='delete_customer'),
     path('search_customer/' , views.search_customer, name='search_customer'),

#                           -------------------- Employee -----------------------

     path('employee_list/' , views.employee_list, name='employee_list'),
     path('add_employee/' , views.add_employee, name='add_employee'),
     path('<int:employee_id>/edit_employee/' , views.edit_employee, name='edit_employee'),
     path('<int:employee_id>/delete_employee/' , views.delete_employee, name='delete_employee'),
     path('search_employee/' , views.search_employee, name='search_employee'),
     path('<int:user_id>/profile_employee/' , views.profile_employee, name='profile_employee'),
     path('<int:user_id>/edit_profile_employee/' , views.edit_profile_employee, name='edit_profile_employee'),

# ------------------------------------------ End Admin Page ----------------------------------------------------
]