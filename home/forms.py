from django import forms
from .models import Contact


# ------------------------------------------ Begin Home Page Forms ----------------------------------------------------

#                           -------------------- Login/Register Form -----------------------

# Login Form
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Tên đăng nhập'}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Mật khẩu'}))
    # remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'type':'checkbox','required':'False'}))
    
# Register Form
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Tên đăng nhập'}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Mật khẩu'}))
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Xác nhận mật khẩu'}))
    email=forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))

#                           -------------------- Contact -----------------------

# Form Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('customer_name','customer_email','content')
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nhập tên','required':''}),
            'customer_email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','required':''}),
            'content': forms.Textarea(attrs={'class': 'form-control','placeholder':'Đừng ngại hỏi về đơn hàng của bạn','required':''}),
        }

# ------------------------------------------ End Home Page Forms ----------------------------------------------------

# ------------------------------------------ Begin Admin Page Forms ----------------------------------------------------

#                           -------------------- Contact -----------------------

# Search Contact Form
class SearchContactForm(forms.Form):
    choices_type=(('Tên khách hàng','Tên khách hàng'),('Email','Email'))
    search_type=forms.CharField(widget=forms.Select(choices=choices_type,attrs={'class':'form-control'}))


# ------------------------------------------ End Admin Page Forms ----------------------------------------------------