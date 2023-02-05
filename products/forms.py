from django import forms
from . models import Category,Comment,Product

#                           -------------------- Product Forms  -----------------------
# Form Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'title', 'category', 'price', 'description','is_active','brand','featured']
        choices_status=(('True','Hoạt động'),('False','Khóa'))
        choices_featured=(('Normal','Bình thường'),('Featured','Nổi bật'),('Best_selling','Bán chạy nhất'),('Favorite','Yêu thích nhất'))
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control',"type":"file"}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tên sản phẩm'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Gía sản phẩm'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Mô tả sản phẩm'}),
            'is_active': forms.Select(choices=choices_status,attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Hãng'}),
            'featured':forms.Select(choices=choices_featured,attrs={'class': 'form-control'})
        }

# Search Product Form
class SearchProductForm(forms.Form):
    choices_type=(('Tên sản phẩm','Tên sản phẩm'),('Thương hiệu','Thương hiệu'))
    search_type=forms.CharField(widget=forms.Select(choices=choices_type,attrs={'class':'form-control'}))

#                           -------------------- Category Forms  -----------------------

# Form Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Loại sản phẩm'})
        }

#                           -------------------- Comment Forms  -----------------------

# Form Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commenter_name','commenter_email','comment_body')
        widgets = {
            'commenter_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nhập tên','required':''}),
            'commenter_email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','required':''}),
            'comment_body': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nhận xét','required':''}),
        }


# Search Product Form
class SearchCommentForm(forms.Form):
    choices_type=(('Tên khách hàng','Tên khách hàng'),('Email','Email'))#,('Sản phẩm','Sản phẩm'))
    search_type=forms.CharField(widget=forms.Select(choices=choices_type,attrs={'class':'form-control'}))