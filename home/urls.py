from django.urls import path
from home import views

urlpatterns = [
# ------------------------------------------ Begin Home Page -------------------------------------------------

#                      -------------------- Login/Register -----------------------
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('register/',views.register, name='register'),

#                      -------------------- Home -----------------------

    path('', views.index,name='home'),

#                      -------------------- Concact -----------------------

    path('contact/', views.contact, name='contact'),

    # path('page_not_found/', views.page_not_found, name='page_not_found'),

# ------------------------------------------ End Home Page ----------------------------------------------------

# ------------------------------------------ Begin Admin Page -------------------------------------------------

#                      -------------------- Admin -----------------------

    path('admin/', views.index_admin, name='admin'),
    
#                      -------------------- Concact -----------------------

    path('contact_list/', views.contact_list, name='contact_list'),
    path('search_contact/', views.search_contact, name='search_contact'),

# ------------------------------------------ End Admin Page ----------------------------------------------------
]