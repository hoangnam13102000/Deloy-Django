from django import forms
from django.contrib.auth.models import User
from .models import Customer,Employee

# ------------------------------------------ Begin Home Page Forms ----------------------------------------------------

#                           -------------------- Customer Forms -----------------------

# Edit info Customer Form 
class Customer_info_Form(forms.ModelForm):
    class Meta:
        model=Customer
        fields= ["fullname","gender","address","phone", "email","username"]
        choices_gender=(('Male','Nam'),('Female','Nữ'))
        widgets={
            'fullname':forms.TextInput(attrs={'class':'form-control','placeholder':'Họ và tên'}),
            'gender': forms.RadioSelect(choices=choices_gender,attrs={'class':'form-check'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Số điện thoại'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Địa chỉ'}),
            'username':forms.TextInput(attrs={'class':'form-control','readonly':''}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }

# Change Password Form
class Change_Password_Form(forms.ModelForm):
    old_password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Mật khẩu cũ'}))
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Xác nhận khẩu'}))
    class Meta:
        model=Customer
        fields= ["password"]
        widgets={
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Mật khẩu mới','required':''}),
        }

#                           -------------------- Employee Forms  -----------------------

# Edit info Employee at Home page 
class Employee_info_Form(forms.ModelForm):
    class Meta:
        model=Employee
        fields= ["image","fullname","gender","address","phone", "email","username"]
        choices_gender=(('Male','Nam'),('Female','Nữ'))
        widgets={
            'image': forms.FileInput(attrs={'class': 'form-control',"type":"file"}),
            'fullname':forms.TextInput(attrs={'class':'form-control','placeholder':'Họ và tên'}),
            'gender': forms.RadioSelect(choices=choices_gender,attrs={'class':'form-check'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Số điện thoại'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Địa chỉ'}),
            'username':forms.TextInput(attrs={'class':'form-control','readonly':''}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }

# Change Password Employee Form at Home page
class Change_Password_Employee_Form(forms.ModelForm):
    old_password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Mật khẩu cũ'}))
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Xác nhận khẩu'}))
    class Meta:
        model=Employee
        fields= ["password"]
        widgets={
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Mật khẩu mới','required':''}),
        }



# ------------------------------------------ End Home Page Forms ----------------------------------------------------

# ------------------------------------------ Begin Admin Page Forms ----------------------------------------------------

#                           -------------------- Customer Forms  -----------------------

# Add Customer Form
class AddCustomerForm(forms.ModelForm):
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Xác nhận mật khẩu','required':''}))
    class Meta:
        model=Customer
        fields= ["fullname","gender","address","phone", "email","username","password"]
        choices_gender=(('Male','Nam'),('Female','Nữ'))
        widgets={
            'fullname':forms.TextInput(attrs={'class':'form-control','placeholder':'Họ và tên'}),
            'gender': forms.RadioSelect(choices=choices_gender,attrs={'class':'form-check'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Số điện thoại'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Địa chỉ'}),
            'username':forms.TextInput(attrs={'class':'form-control','required':'','placeholder':'Tên tài khoản'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Mật khẩu','required':''}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','required':''}),
        }

# Edit Customer Form  
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields= ["fullname","gender","address","phone", "email","username","password","is_active"]
        choices_gender=(('Male','Nam'),('Female','Nữ'))
        choices_status=(('True','Hoạt động'),('False','Khóa'))
        widgets={
            'fullname':forms.TextInput(attrs={'class':'form-control','placeholder':'Họ và tên'}),
            'gender': forms.RadioSelect(choices=choices_gender,attrs={'class':'form-check'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control','readonly':'','required':''}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Mật khẩu','required':''}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','required':''}),
            "is_active":forms.Select(choices=choices_status,attrs={'class': 'form-control'}),
        }

# Search Employee Form
class SearchCustomerForm(forms.Form):
    choices_type=(('Họ tên','Họ tên'),('username','username'),('Số điện thoại','Số điện thoại'),('email','email'),('Địa chỉ','Địa chỉ'))
    search_type=forms.CharField(widget=forms.Select(choices=choices_type,attrs={'class':'form-control'}))

#                           -------------------- Employee Forms  -----------------------

# Add Employee Form
class AddEmployeeForm(forms.ModelForm):
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Xác nhận mật khẩu','required':''}))
    class Meta:
        model=Employee
        fields= ["image","fullname","gender","address","phone", "email","username","password","salary","position"]
        choices_gender=(('Male','Nam'),('Female','Nữ'))
        choices_position=(('Staff','Nhân viên'),('Admin','Quản lý'))
        widgets={
            'image': forms.FileInput(attrs={'class': 'form-control',"type":"file"}),
            'fullname':forms.TextInput(attrs={'class':'form-control','placeholder':'Tên nhân viên'}),
            'gender': forms.RadioSelect(choices=choices_gender,attrs={'class':'form-check'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Số điện thoại'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Địa chỉ'}),
            'username':forms.TextInput(attrs={'class':'form-control','required':'','placeholder':'Tên tài khoản'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Mật khẩu','required':''}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','required':''}),
            "salary":forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Lương nhân viên'}),
            "position":forms.Select(choices=choices_position,attrs={'class': 'form-control'}),
        }

# Edit EmployeeForm Form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields= ["image","fullname","gender","address","phone", "email","username","password","salary","position","is_active"]
        choices_gender=(('Male','Nam'),('Female','Nữ'))
        choices_position=(('Staff','Nhân viên'),('Admin','Quản lý'))
        choices_status=(('True','Hoạt động'),('False','Khóa'))
        widgets={
            'image': forms.FileInput(attrs={'class': 'form-control',"type":"file"}),
            'fullname':forms.TextInput(attrs={'class':'form-control','placeholder':'Họ và tên'}),
            'gender': forms.RadioSelect(choices=choices_gender,attrs={'class':'form-check'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control','readonly':'','required':''}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Mật khẩu','required':''}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','required':''}),
            "salary":forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Lương nhân viên'}),
            "position":forms.Select(choices=choices_position,attrs={'class': 'form-control'}),
            "is_active":forms.Select(choices=choices_status,attrs={'class': 'form-control'}),
        }

# View & Edit ProfileEmployee Form
class ProfileEmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields= ["image","fullname","gender","address","phone", "email","username","password","salary","position"]
        choices_gender=(('Male','Nam'),('Female','Nữ'))
        widgets={
            'image': forms.FileInput(attrs={'class': 'form-control',"type":"file"}),
            'fullname':forms.TextInput(attrs={'class':'form-control','placeholder':'Họ và tên'}),
            'gender': forms.RadioSelect(choices=choices_gender,attrs={'class':'form-check'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control','required':'','readonly':''}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Mật khẩu','required':''}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','required':'','aria-describedby':'basic-addon1'}),
            "salary":forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Lương nhân viên','readonly':''}),
            "position":forms.TextInput(attrs={'class': 'form-control','readonly':'' }),
        }

# Search Employee Form
class SearchEmployeeForm(forms.Form):
    choices_type=(('Họ tên','Họ tên'),('username','username'),('Số điện thoại','Số điện thoại'),('email','email'),('Địa chỉ','Địa chỉ'))
    search_type=forms.CharField(widget=forms.Select(choices=choices_type,attrs={'class':'form-control'}))

# ------------------------------------------ End Admin Page Forms ----------------------------------------------------