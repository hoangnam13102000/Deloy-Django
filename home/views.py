from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact
from .forms import ContactForm,SearchContactForm, LoginForm, RegisterForm
from users.models import Customer,Employee
from products.forms import Product, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout,get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.conf.urls import handler404
from .serializers import ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# ------------------------------------------ Begin Home Page ----------------------------------------------------

# Home page
def index(request):
    # Title Web
    title_web="Trang chủ"
    
    # # show navbar in home page
    categories=Category.objects.all()
    
    # view featured product and pagination page
    product_featured = Product.objects.filter(featured='Featured',is_active=True).all()
    paginator = Paginator( product_featured, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # view best selling product and pagination page
    product_best_selling = Product.objects.filter(featured='Best_selling',is_active=True).all()
    paginator1 = Paginator(product_best_selling, 3)
    page_number1 = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number1)
    
    # view favorite product and pagination page 
    product_favorite_product = Product.objects.filter(featured='Favorite',is_active=True).all()
    paginator2 = Paginator(product_favorite_product, 2)
    page_number2 = request.GET.get('page')
    page_obj2 = paginator2.get_page(page_number2)
    
    # view cart
    cart_items = []
    total = 0
    if 'cart' in request.session:
        for item in request.session['cart']:
            # product = get_object_or_404(Product, pk=item['id'])
            item['total_price'] = item['price'] * item['quantity']
            total += item['total_price']
            cart_items.append(item)
    
    context={
        'title_web':title_web,
        'page_obj': page_obj,
        'categories':categories,
        'page_obj1': page_obj1,
        'page_obj2': page_obj2,
        'cart_items': cart_items
    }
    return render(request,'home/pages/index.html',context)

# Login page
def login(request):
     # Title Web
    title_web="Đăng nhập"
    
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        # remember_me = request.POST['remember_me']
        account =authenticate(request, username=username,password=password )
        if(account is not None):
            get_user= get_user_model()
            user=get_user.objects.get(username= username)
            if(user.is_staff == True):
                # if not remember_me:
                #     request.session.set_expiry(0)
                messages.success(request,'Đăng nhập trang Admin thành công')
                auth_login(request,user)
                return redirect('admin')
            else:
                # if not remember_me:
                #     request.session.set_expiry(0)
                auth_login(request,user)
                messages.success(request,'Đăng nhập thành công')
                return redirect('home')
        else:
            messages.error(request,'Tài khoản hoặc mật khẩu không đúng!')
            return redirect('login')
    else:
        # show navbar in home page
        categories=Category.objects.all()
        form=LoginForm()
    
    context={
        'title_web':title_web,
        'categories':categories,
        'form':form
    }
    return render(request,'home/pages/account/login.html', context)

# Register page
def register(request):
    # Title Web
    title_web="Đăng ký"
    
    if(request.method=="POST"):
        form=RegisterForm(request.POST)
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if(User.objects.filter(username=username)):
            messages.error(request,'Tên đăng nhập đã tồn tại!')
            return redirect('register')
        if(User.objects.filter(email=email)):
            messages.error(request,'Email đã tồn tại!')
            return redirect('register')
        if(password!=password2):
             messages.error(request,'Mật khẩu không trùng nhau!')
             return redirect('register')
        if(form.is_valid()):
            User.objects.create_user(username,email,password)
            account=Customer(username=username,email=email,password=password)
            account.save()
            messages.success(request,'Đăng ký tài khoản thành công')
            return redirect('login')
    else:
        # show navbar in home page
        categories=Category.objects.all()
        form=RegisterForm()
    
    context={
        'title_web':title_web,
        'categories':categories,
        'form':form
    }
    return render(request,'home/pages/account/register.html',context)

# Logout
def logout(request):
    auth_logout(request)
    messages.success(request,'Đăng xuất thành công')
    return redirect('/')

# Contact page
def contact(request):
    # Title Web
    title_web="Liên hệ"
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ContactForm(request.POST)
            user= request.user
            customer = Customer.objects.filter(username=user.username).first()
            if form.is_valid():
                new_form = form.save(commit=False) # không thực hiện lưu đối tượng ngay lập tức mà thay vào đó có thể chỉnh sửa giá trị trước khi lưu.
                new_form.username = customer
                new_form.save()
                messages.success(request,'Phản hồi của bạn đã được gửi')
                return redirect('contact')     
        else:
            messages.error(request,'Bạn cần đăng nhập để liên hệ với chúng tôi!')
            return redirect('login')
    else:
        # show navbar in home page
        categories=Category.objects.all()
        form = ContactForm()
    
    context={
        'title_web':title_web,
        'categories':categories,
        'form':form
    }
    return render(request,'home/pages/contact.html',context)


# ERROR NOT FOUND PAGE
# def page_not_found(request):
#     return render(request, 'home/404.html')

# def page_not_found(request, exception):
#     return render(request, 'home/pages/404.html', {}, status=404)
# handler404 = page_not_found

# ------------------------------------------ End Home Page ----------------------------------------------------

# ------------------------------------------ Begin Admin Page ----------------------------------------------------

def index_admin(request):
    # Title Web
    title_web="Trang chủ | Admin "
    
    #show admin web user information
    user=request.user
    profie_employee  =Employee.objects.filter(username=user.username).first()
    
    # view customer list and pagination
    cusromers = Customer.objects.all()
    paginator = Paginator(cusromers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # view product list and pagination
    products = Product.objects.all()
    paginator1 = Paginator(products, 5)
    page_number1 = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number1)
    
    context={
        'title_web':title_web,
        'page_obj': page_obj,
        'page_obj1': page_obj1,
        'profie_employee':profie_employee 
    }
    return render(request,'admin/index.html',context)


# Show list Contact 
def contact_list(request):
    # Title Web
    title_web="Quản lý phản hồi"
    
    #show admin web user information
    user=request.user
    profie_employee  =Employee.objects.filter(username=user.username).first()
    
    # search form in contact list
    search_form= SearchContactForm()
    
    # view contacts list and pagination
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={
        'title_web':title_web,
        'page_obj': page_obj,
        'profie_employee':profie_employee ,
        'search_form':search_form
    }
    return render(request, 'admin/contact_manager/contact_list.html', context)


# Search Contact
def search_contact(request):
    # Title Web
    title_web="Tìm kiếm phản hồi"
    
    #show admin web user information
    user=request.user
    profie_employee  =Employee.objects.filter(username=user.username).first()
    
    search_type=request.GET.get('search_type')
    keyword = request.GET.get('keyword')
    search_form= SearchContactForm()
    if search_type == "Email":
        data = Contact.objects.filter(customer_email__icontains=keyword).order_by('-id')
    else:
        data = Contact.objects.filter(customer_name__icontains=keyword).order_by('-id')

    context={
        'title_web':title_web,
        'profie_employee':profie_employee ,
        'data':data,
        'search_form':search_form
    }
    return render(request, 'admin/contact_manager/search_contact.html', context)

# ------------------------------------------ End Admin Page ----------------------------------------------------

# ------------------------------------------ Begin RestAPI ----------------------------------------------------

# RestAPI Contact
class  Contact_API_View(APIView):
    def get(self,request):
        listContact= Contact.objects.all()
        Contactdata= ContactSerializer(listContact, many=True).data # Adding .data to convert the data from ListSerializer to JSON
        return Response(data= Contactdata, status=status.HTTP_200_OK)
    
# ------------------------------------------ End RestAPI ----------------------------------------------------