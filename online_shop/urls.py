"""mobie_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from users.views import Customer_API_View
# from products.views import Product_API_View,Category_API_View,Comment_API_View
# from order.views import Order_API_View
# from home.views import Contact_API_View

# from django.conf.urls import handler404

# handler404 = 'home.error_views.page_not_found'
urlpatterns = [
    path('django/', admin.site.urls),
    path('',include('home.urls'),name='home'),  
    path('user/',include('users.urls'),name='user'), 
    path('product/',include('products.urls'),name='product'),
    path('order/',include('order.urls'),name='order'),
    
    # Rest_API
    # path('customer_api/',Customer_API_View.as_view()),
    # path('product_api/',Product_API_View.as_view()),
    # path('category_api/',Category_API_View.as_view()),
    # path('comment_api/',Comment_API_View.as_view()),
    # path('order_api/',Order_API_View.as_view()),
    # path('contact_api/', Contact_API_View.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
