from django.shortcuts import render,redirect, get_object_or_404 # calls the given model and get object from that if that object or model doesn’t exist it raise 404 error.
from .forms import CustomerForm,Customer_info_Form,Change_Password_Form
from django.contrib import messages
from .models import Customer, Employee
from .forms import AddCustomerForm,AddEmployeeForm,EmployeeForm,ProfileEmployeeForm,SearchEmployeeForm,SearchCustomerForm,Employee_info_Form,Change_Password_Employee_Form
from . utils import handle_upload_file
from .serializers import CustomerSerializer #,CustomerCreationSerializer
from products.models import Category
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# ------------------------------------------ Begin Home Page ----------------------------------------------------

#                           -------------------- Customer -----------------------

# View profile customer
def profile_user(request,user_id):
    # Title Web
    title_web="Thông tin người dùng"
    
    # show navbar in home page
    categories=Category.objects.all()
    
    user = get_object_or_404(User, id=user_id)
    if (user.is_staff):
        employee=Employee.objects.filter(username=user.username).first()
        context={
            'title_web':title_web,
            'customer':employee,
            'categories':categories
        }
        return render(request, 'home/pages/profile_user/profile_user.html', context)
    else:
        customer=Customer.objects.filter(username=user.username).first() #first() takes a query set and returns the first element
        context={
            'title_web':title_web,
            'customer':customer,
            'categories':categories
        }
        return render(request, 'home/pages/profile_user/profile_user.html', context)

# edit customer
def edit_profile_user(request,user_id):
    # Title Web
    title_web="Cập nhập thông tin"
    
    # show navbar in home page
    categories=Category.objects.all()
    
    user = get_object_or_404(User, id=user_id)
    if (user.is_staff):
        employee=Employee.objects.filter(username=user.username).first() #first() takes a query set and returns the first element
        if(request.method=="POST"):
            form =Employee_info_Form(request.POST, request.FILES,instance=employee)
            if form.is_valid():
                handle_upload_file(request.FILES['image'])
                form.save()
                messages.success(request,'Đã cập nhập khách hàng thành công')
                return redirect("home")
        else:
            form = Employee_info_Form(instance=employee)
        context={
            'title_web':title_web,
            'form':form,
            'categories':categories
        }
        return render(request, 'home/pages/profile_user/edit_profile_user.html', context)
    else:
        customer=Customer.objects.filter(username=user.username).first() #first() takes a query set and returns the first element
        if(request.method=="POST"):
            form =Customer_info_Form(request.POST,instance=customer)
            if form.is_valid():
                form.save()
                messages.success(request,'Đã cập nhập khách hàng thành công')
                return redirect("home")
            # print(form.errors) #print error of form
        else:
            form = Customer_info_Form(instance=customer)

        context={
            'title_web':title_web,
            'form':form,
            'categories':categories
        }
        return render(request, 'home/pages/profile_user/edit_profile_user.html', context)

# Change password
def change_password(request,user_id):
    # Title Web
    title_web="đổi mật khẩu"
    
    # show navbar in home page
    categories=Category.objects.all()
    
    user = get_object_or_404(User, id=user_id)
    if (user.is_staff):
        # Change password for employee
        employee=Employee.objects.filter(username=user.username).first() #first() takes a query set and returns the first element
        form =Change_Password_Employee_Form(request.POST)
        
        if form.is_valid():
            new_password=request.POST['password']
            old_password=request.POST['old_password']
            password2=request.POST['password2']
            if(employee.password == old_password):
                if(old_password==new_password):
                    messages.error(request,'Mật khẩu mới không được trùng với mật khẩu cũ!')
                    return redirect('change_password', id=user.id)
                else:
                    if(new_password!=password2):
                        messages.error(request,'Mật khẩu không trùng nhau!')
                        return redirect('change_password', id=user.id)
                    else:
                        employee.password=new_password
                        employee.save()
                        
                        new_password=make_password(new_password,hasher='default')
                        user.password=new_password
                        user.save()
                        messages.success(request,'Đã đổi mật khẩu thành công!. Mời quý khách đăng nhập lại.')
                        return redirect("home")
            else:
                messages.error(request,'Sai mật khẩu!')
                return redirect('change_password', id=user.id)
        form =Change_Password_Employee_Form()
        
        context={
            'title_web':title_web,
            'form':form,
            'categories':categories
        }
        return render(request, 'home/pages/account/change_password.html',context)
    else:
        # Change password for customer
        customer=Customer.objects.filter(username=user.username).first()
        form =Change_Password_Form(request.POST)
        if form.is_valid():
            new_password=request.POST['password']
            old_password=request.POST['old_password']
            password2=request.POST['password2']
            if(customer.password == old_password):
                if(old_password==new_password):
                    messages.error(request,'Mật khẩu mới không được trùng với mật khẩu cũ!')
                    return redirect('change_password', id=user.id)
                else:
                    if(new_password!=password2):
                        messages.error(request,'Mật khẩu không trùng nhau!')
                        return redirect('change_password', id=user.id)
                    else:
                        customer.password=new_password
                        customer.save()
                        
                        new_password=make_password(new_password,hasher='default')
                        user.password=new_password
                        user.save()
                        messages.success(request,'Đã đổi mật khẩu thành công!. Mời quý khách đăng nhập lại.')
                        return redirect("home")
            else:
                messages.error(request,'Sai mật khẩu!')
                return redirect('change_password', id=user.id)
        form =Change_Password_Form()
        
        context={
            'title_web':title_web,
            'form':form,
            'categories':categories
        }
        return render(request, 'home/pages/account/change_password.html',context)

# ------------------------------------------ End Home Page ----------------------------------------------------

# ------------------------------------------ Begin Admin Page ----------------------------------------------------

#                           -------------------- Customer -----------------------

# Show Customer list
def customer_list(request):
    # Title Web
    title_web="Danh sách khách hàng"
    
    #show admin web user information
    user=request.user
    profie_employee  =Employee.objects.filter(username=user.username).first()
    
    search_form= SearchCustomerForm()
    
    # All customer in list and pagination
    customer = Customer.objects.all()
    paginator = Paginator(customer, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={
        'title_web':title_web,
        'page_obj':page_obj,
        'profie_employee':profie_employee ,
        'search_form':search_form
    }
    return render(request, 'admin/user_manager/customers/customer_list.html', context)

# add info customer
def add_user(request):
    # Title Web
    title_web="Thêm khách hàng"
    
    if(request.method=="POST"):
        form=AddCustomerForm(request.POST)
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        fullname=request.POST['fullname']
        phone=request.POST['phone']
        address=request.POST['address']
        gender=request.POST['gender']
        
        if(User.objects.filter(username=username)):
            messages.error(request,'Tên đăng nhập đã tồn tại!')
            return redirect('add_user')
        if(User.objects.filter(email=email)):
            messages.error(request,'Email đã tồn tại!')
            return redirect('add_user')
        if(password!=password2):
             messages.error(request,'Mật khẩu không trùng nhau!')
             return redirect('add_user')
        if(form.is_valid()):
            User.objects.create_user(username,email,password)
            account=Customer(fullname=fullname,phone=phone,username=username,
                             email=email,password=password,address=address,gender=gender)
            account.save()
            messages.success(request,'Thêm khách hàng thành công')
            return redirect('customer_list')
    else:
        # show admin web user information
        user=request.user
        profie_employee =Employee.objects.filter(username=user.username).first()
        # Add Customer Form
        form=AddCustomerForm()
    
    context={
        'title_web':title_web,
        'form':form,
        'profie_employee':profie_employee
    }
    return render(request,'admin/user_manager/customers/add_customer.html',context)

# Edit customer
def edit_customer_admin(request,customer_id):
    # Title Web
    title_web="Cập nhập thông tin khách hàng"
    
    customer = get_object_or_404(Customer, id=customer_id)
    user=User.objects.filter(username=customer.username).first()
    
    if request.method == 'POST':
        form =CustomerForm(request.POST or None,instance=customer)
        new_password = request.POST.get('password')
        is_active=request.POST.get('is_active')
        if form.is_valid():
            # Save account customer
            form.save()
            
            # Save account auth user
            user.email = request.POST.get('email')
            password=make_password(new_password,hasher='default')
            user.password=password
            user.is_active=is_active
            user.save()
            
            messages.success(request,'Đã cập nhập khách hàng thành công')
            return redirect("customer_list")
    else:
        # show admin web user information
        user=request.user
        profie_employee =Employee.objects.filter(username=user.username).first()
        
        form = CustomerForm(instance=customer)

    context={
        'title_web':title_web,
        'form':form,
        'profie_employee':profie_employee,
        'customer':customer
    }
    return render(request, 'admin/user_manager/customers/edit_customer.html', context)

# Delete customer 
def delete_customer(request,customer_id):
    customer=Customer.objects.get(id=customer_id)
    account=User.objects.filter(username=customer.username)
    account.delete()
    customer.delete()
    messages.success(request,'Xóa khách hàng thành công')
    return redirect('customer_list')

# Search customer
def search_customer(request):
    # Title Web
    title_web="Tìm kiếm khách hàng"
    
    #show admin web user information
    user=request.user
    profie_employee =Employee.objects.filter(username=user.username).first()
    
    search_type=request.GET.get('search_type')
    keyword = request.GET.get('keyword')
    search_form= SearchCustomerForm()
    
    if search_type == "email":
        data = Customer.objects.filter(email__icontains=keyword).order_by('-id')
    elif search_type == "username":
        data = Customer.objects.filter(username__icontains=keyword).order_by('-id')
    elif search_type == "Số điện thoại":
        data = Customer.objects.filter(phone__icontains=keyword).order_by('-id')
    elif search_type == "Địa chỉ":
        data = Customer.objects.filter(address__icontains=keyword).order_by('-id')
    else:
        data = Customer.objects.filter(fullname__icontains=keyword).order_by('-id')

    context={
        'title_web':title_web,
        'profie_employee':profie_employee,
        'data':data,
        'search_form':search_form
    }
    return render(request, 'admin/user_manager/customers/search_customer.html',context)

#                           -------------------- Employee -----------------------

# Show Employee list
def employee_list(request):
    # Title Web
    title_web="Danh sách nhân viên"
    
    user=request.user
    profie_employee=Employee.objects.filter(username=user.username).first()
    
    search_form= SearchEmployeeForm()
    
    # All employee in list and pagination
    employees = Employee.objects.all()
    paginator = Paginator(employees , 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={
        'title_web':title_web,
        'page_obj':page_obj,
        'profie_employee':profie_employee,
        'search_form':search_form
    }
    return render(request, 'admin/user_manager/employees/employee_list.html', context)

# add Employee
def add_employee(request):
    # Title Web
    title_web="Thêm nhân viên"
    
    if(request.method=="POST"):
        form=AddEmployeeForm(request.POST, request.FILES)
        image=request.FILES['image']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        fullname=request.POST['fullname']
        phone=request.POST['phone']
        address=request.POST['address']
        gender=request.POST['gender']
        position=request.POST['position']
        salary=request.POST['salary']
        
        if(User.objects.filter(username=username)):
            messages.error(request,'Tên đăng nhập đã tồn tại!')
            return redirect('add_employee')
        if(User.objects.filter(email=email)):
            messages.error(request,'Email đã tồn tại!')
            return redirect('add_employee')
        if(password!=password2):
             messages.error(request,'Mật khẩu không trùng nhau!')
             return redirect('add_employee')
        if(form.is_valid()):
            handle_upload_file(image)
            
            # Add account auth user
            user=User.objects.create_user(username,email,password )
            user.is_staff = True
            user.is_superuser = True if position == 'Admin' else False
            user.save()
            
            # Add account employee
            account=Employee(image=image,username=username,email=email,password=password,fullname=fullname
                             ,phone=phone,address=address,gender=gender,position=position,salary=salary)
            account.save()
            
            messages.success(request,'Tạo nhân viên thành công')
            return redirect('employee_list')
    else:
        #show admin web user information
        user=request.user
        profie_employee =Employee.objects.filter(username=user.username).first()
        
        form=AddEmployeeForm()
    
    context={
        'title_web':title_web,
        'form':form,
        'profie_employee':profie_employee,
    }
    return render(request,'admin/user_manager/employees/add_employee.html',context)

# Edit employee
def edit_employee(request,employee_id):
    # Title Web
    title_web="Câp nhập thông tin nhân viên"
    
    employee = get_object_or_404(Employee, id=employee_id)
    user=User.objects.filter(username=employee.username).first()
    # customer=Customer.objects.filter(username=employee.username).first()
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            handle_upload_file(request.FILES['image'])
            # Save account employee
            form.save()
            
            # Save account auth user
            user.is_superuser = True if request.POST.get('position') == 'Admin' else False
            user.email = request.POST.get('email')
            password=make_password(request.POST.get('password'),hasher='default')
            user.password=password
            user.is_active=request.POST.get('is_active')
            user.save()
            
            messages.success(request,'Đã cập nhập nhân viên thành công')
            return redirect('employee_list')

    else:
        #show admin web user information
        user=request.user
        profie_employee =Employee.objects.filter(username=user.username).first()
        form = EmployeeForm(instance=employee)
    
    context={
        'title_web':title_web,
        'employee':employee,
        'form':form,
        'profie_employee':profie_employee
    }
    return render(request, 'admin/user_manager/employees/edit_employee.html', context)

# Delete employee 
def delete_employee(request,employee_id):
    
    employee=Employee.objects.get(id=employee_id)
    employee.delete()
    
    user_auth=User.objects.filter(username=employee.username)
    user_auth.delete()
    
    messages.success(request,'Xóa nhân viên thành công')
    
    return redirect('employee_list')

# Search Employee
def search_employee(request):
    # Title Web
    title_web="Tìm kiếm nhân viên"
    
    #show admin web user information
    user=request.user
    profie_employee =Employee.objects.filter(username=user.username).first()
    
    search_type=request.GET.get('search_type')
    keyword = request.GET.get('keyword')
    search_form= SearchEmployeeForm()
    if search_type == "email":
        data = Employee.objects.filter(email__icontains=keyword).order_by('-id')
    elif search_type == "username":
        data = Employee.objects.filter(username__icontains=keyword).order_by('-id')
    elif search_type == "Số điện thoại":
        data = Employee.objects.filter(phone__icontains=keyword).order_by('-id')
    elif search_type == "Địa chỉ":
        data = Employee.objects.filter(address__icontains=keyword).order_by('-id')
    else:
        data = Employee.objects.filter(fullname__icontains=keyword).order_by('-id')

    context={
        'title_web':title_web,
        'profie_employee':profie_employee,
        'data':data,
        'search_form':search_form
    }
    return render(request, 'admin/user_manager/employees/search_employee.html',context)

# Show Profile employee
def profile_employee(request,user_id):
    # Title Web
    title_web="Thông tin người dùng"
    
    #show admin web user information
    user_admin=request.user
    profie_employee =Employee.objects.filter(username=user_admin.username).first()
    
    employee = get_object_or_404(Employee, id=user_id)

    context={
        'title_web':title_web,
        'profie_employee':profie_employee,
        'employee':employee, 
    }
    return render(request, 'admin/user_manager/employees/profile_employee/profile_employee.html', context)

# Edit Profile employee
def edit_profile_employee(request,user_id):
    # Title Web
    title_web="Cập nhập thông tin người dùng"
    
    employee = get_object_or_404(Employee, id=user_id)
    user=User.objects.filter(username=employee.username).first()
    
    if request.method == 'POST':
        form = ProfileEmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            # Sace account employee
            form.save()
            # Save account auth user
            user.email = request.POST.get('email')
            password=make_password(request.POST.get('password'),hasher='default')
            user.password=password
            user.save()
            
            messages.success(request,'Đã cập nhập thông tin thành công, mời bạn đăng nhập lại')
            return redirect('home')
    else:
        #show admin web user information
        user_admin=request.user
        profie_employee =Employee.objects.filter(username=user_admin.username).first()
        form = ProfileEmployeeForm(instance=employee)

    context={
        'title_web':title_web,
        'profie_employee':profie_employee,
        'form':form,
        'employee':employee, 
    }
    return render(request, 'admin/user_manager/employees/profile_employee/edit_profile_employee.html', context)

# ------------------------------------------ End Admin Page ----------------------------------------------------

# ------------------------------------------ Begin RestAPI ----------------------------------------------------

# RestAPI Customer
class Customer_API_View(APIView):
    def get(self,request):
        listCustomer=Customer.objects.all()
        Customerdata=CustomerSerializer(listCustomer, many=True).data # Adding .data to convert the data from ListSerializer to JSON
        return Response(data=Customerdata, status=status.HTTP_200_OK)
    # def post(self,request):
    #     Customerdata=CustomerCreationSerializer(data=request.data)
        
    #     if(not Customerdata.is_valid()):
    #         return Response('Dữ liệu bị sai !', status=status.HTTP_400_BAD_REQUEST)





# ------------------------------------------ End RestAPI ----------------------------------------------------