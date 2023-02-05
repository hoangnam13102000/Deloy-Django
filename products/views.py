from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from users.models import Employee
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import  Category,Product,Comment
from . forms import CategoryForm,ProductForm,CommentForm, SearchProductForm, SearchCommentForm
from . utils import handle_upload_file
from .serializers import ProductSerializer,CategorySerializer,CommentSerializer #,CustomerCreationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# ------------------------------------------ Begin Home Page ----------------------------------------------------

#                           -------------------- Product -----------------------

# View Product detail in home page by id
def product_detail(request, product_id):
    # Title Web
    title_web="Chi tiết sản phẩm"
    
    # comment product
    product = get_object_or_404(Product, pk=product_id)
    comments= product.comments.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.product = product
                comment.save()
                return redirect('product_detail', id)     
        else:
            messages.error(request,'Bạn cần đăng nhập để bình luận!')
    else:
        # show navbar in home page
        categories=Category.objects.all()
        # Coment Product Form
        form = CommentForm()
    
    context={
        'title_web':title_web,
        'product': product,
        'categories':categories,
        'form': form,
        'comments':comments
    }
    return render(request, 'home/pages/products/product_detail.html',context)

# Show product depend on category.id
def product_of_category(request, category_id):
    # get id of category from navbar
    category = get_object_or_404(Category, id=category_id)
    
    # Title Web
    title_web=category.name
    
    # show navbar in home page
    categories=Category.objects.all()
    
    # view all products and pagination depend on category.id
    product=Product.objects.filter(category=category).all()
    paginator = Paginator(product, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={
        'title_web':title_web,
        'page_obj':page_obj,
        'categories':categories,
        'category':category
    }
    return render(request, 'home/pages/products/shop_product_list.html', context)

# Search product
def search_products(request):
    # Title Web
    title_web="Tìm kiếm sản phẩm"
    
    # show navbar in home page
    categories=Category.objects.all()
    
    # search product depend on product_title by keyword
    keyword = request.GET.get('keyword')
    data = Product.objects.filter(title__icontains=keyword).order_by('-id')
    
    context={
        'title_web':title_web,
        'data': data,
        'categories':categories
    }
    return render(request, 'home/pages/products/search.html', context)

# ------------------------------------------ End Home Page ----------------------------------------------------

# ------------------------------------------ Begin Admin Page ----------------------------------------------------

#                           -------------------- Category -----------------------

# Show Category list
def category_list(request):
    # Title Web
    title_web='Danh sách loại sản phẩm'
    
    #show admin web user information
    user=request.user
    profie_employee =Employee.objects.filter(username=user.username).first()
    
    # view all categories and pagination
    categories = Category.objects.all()
    paginator = Paginator(categories, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={
        'title_web':title_web,
        'page_obj': page_obj,
        'profie_employee':profie_employee
    }
    return render(request, 'admin/product_manager/categories/category_list.html', context)

# Add Category
def addCategory(request):
    # Title Web
    title_web='Thêm loại sản phẩm'
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        name=request.POST['name']
        if(Category.objects.filter(name=name)):
            messages.error(request,'Loại sản phẩm đã tồn tại!')
            return redirect('addCategory')
        if form.is_valid():
            form.save()
            messages.success(request,'Thêm loại sản phẩm thành công')
            return redirect('category_list')
    else:
        #show admin web user information
        user=request.user
        profie_employee =Employee.objects.filter(username=user.username).first()
        # Add Category Form
        form = CategoryForm()

    context={
        'title_web':title_web,
        'form':form,
        'profie_employee':profie_employee
    }
    return render(request, 'admin/product_manager/categories/add_category.html', context)

# Edit Category by id
def edit_category(request,category_id):
    # Title Web
    title_web='Cập nhập loại sản phẩm'
    
    #show admin web user information
    user=request.user
    profie_employee =Employee.objects.filter(username=user.username).first()
    
    category=get_object_or_404(Category, id=category_id)
    form =CategoryForm(request.POST,instance=category)
    if form.is_valid():
        form.save()
        messages.success(request,'Cập nhập thông tin thành công')
        return redirect("edit_category",id=category.id)
    else:
        form = CategoryForm(instance=category)

    context={
        'title_web':title_web,
        'form': form,
        'profie_employee':profie_employee,
        'category':category
    }
    return render(request, 'admin/product_manager/categories/edit_category.html', context)

# Delete Category by id
def delete_category(request, category_id):
    # get id category 
    category = Category.objects.get(id=category_id)
    # Delete category
    category.delete()
    messages.success(request,'Xóa loại sản phẩm thành công')
    return redirect('category_list')

# Search Category
def search_category(request):
    # Title Web
    title_web='Tìm kiếm loại sản phẩm'
    
    #show admin web user information
    user=request.user
    profie_employee =Employee.objects.filter(username=user.username).first()
    
    keyword = request.GET.get('keyword')
    data = Category.objects.filter(name__icontains=keyword).order_by('-id')
    
    context={
        'title_web':title_web,
        'profie_employee':profie_employee,
        'data':data,
    }
    return render(request, 'admin/product_manager/categories/search_category.html', context)

#                           -------------------- Product -----------------------

# Show list Product admin
def product_list(request):
    # Title Web
    title_web='Danh sách sản phẩm'
    
    #show admin web user information
    user=request.user
    profie_employee =Employee.objects.filter(username=user.username).first()
    
    # search form
    search_form= SearchProductForm()
    
    # view product list and pagination
    products = Product.objects.all()
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={
        'title_web':title_web,
        'page_obj': page_obj,
        'profie_employee':profie_employee,
        'search_form':search_form
    }
    return render(request, 'admin/product_manager/products/list_product.html', context)


# Add product into list
def add_product(request):
    # Title Web
    title_web='Thêm sản phẩm'
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            handle_upload_file(request.FILES['image'])
            product = form.save(commit=False)
            product.category = form.cleaned_data['category']
            product.save()
            messages.success(request,'Thêm sản phẩm thành công')
            return redirect('product_list')
        else:
            messages.error(request,'Thêm sản phẩm thất bại')
    else:
        #show admin web user information
        user=request.user
        profie_employee =Employee.objects.filter(username=user.username).first()
        form = ProductForm()

    context={
        'title_web':title_web,
        'form':form,
        'profie_employee':profie_employee,
    }
    return render(request, 'admin/product_manager/products/add_product.html', context)

# Edit product
def edit_product(request, product_id):
    # Title Web
    title_web='Cập nhập sản phẩm'
    
    #show admin web user information
    user=request.user
    profie_employee =Employee.objects.filter(username=user.username).first()
    
    product = get_object_or_404(Product, id=product_id)
    form =ProductForm(request.POST, request.FILES,instance=product)
    
    if form.is_valid():
        handle_upload_file(request.FILES['image'])
        form.save()
        messages.success(request,'Đã cập nhập sản phẩm thành công')
        return redirect("edit_product", id=product.id)
    else:
        form = ProductForm(instance=product)

    context={
        'title_web':title_web,
        'profie_employee':profie_employee,
        'form': form,
        'product':product,
    }
    return render(request, 'admin/product_manager/products/edit_product.html',context)

# Delete product
def delete_product(request, product_id):
    # get id product 
    product = Product.objects.get(id=product_id)
    # Delete product
    product.delete()
    messages.success(request,'Xóa sản phẩm thành công')
    return redirect('product_list')

# Search product admin
def search_product_admin(request):
    # Title Web
    title_web='Tìm kiếm sản phẩm'
    
    #show admin web user information
    user=request.user
    profie_employee =Employee.objects.filter(username=user.username).first()
    
    search_type=request.GET.get('search_type')
    keyword = request.GET.get('keyword')
    search_form= SearchProductForm()
    if search_type == "Thương hiệu":
        data = Product.objects.filter(brand__icontains=keyword).order_by('-id')
    else:
        data = Product.objects.filter(title__icontains=keyword).order_by('-id')

    context={
        'title_web':title_web,
        'profie_employee':profie_employee,
        'data':data,
        'search_form':search_form,
    }
    return render(request, 'admin/product_manager/products/search_product.html',context)

#                           -------------------- Comment -----------------------

# Show list Comment admin
def comment_list(request):
    # Title Web
    title_web='Danh sách bình luận'
    
    #show web user information
    user=request.user
    profie_employee =Employee.objects.filter(username=user.username).first()
    
    search_form= SearchCommentForm()
    
    # view comments list and pagination
    comments = Comment.objects.all()
    paginator = Paginator(comments, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={
        'title_web':title_web,
        'profie_employee':profie_employee,
        'page_obj': page_obj,
        'search_form':search_form
    }
    return render(request, 'admin/product_manager/comments/comment_list.html', context)

# Delete comment
def delete_comment(request, comment_id):
    # get id comment 
    comment = Comment.objects.get(id=comment_id)
    # Delete comment
    comment.delete()
    messages.success(request,'Xóa bình luận thành công')
    return redirect('comment_list')

def search_comment(request):
    # Title Web
    title_web='Tìm kiếm bình luận'
    
    #show admin web user information
    user=request.user
    profie_employee =Employee.objects.filter(username=user.username).first()
    
    search_type=request.GET.get('search_type')
    keyword = request.GET.get('keyword')
    search_form= SearchCommentForm()
    
    if search_type == "Email":
        data = Comment.objects.filter(commenter_email__icontains=keyword).order_by('-id')
    else:
        data = Comment.objects.filter(commenter_name__icontains=keyword).order_by('-id')

    context={
        'title_web':title_web,
        'profie_employee':profie_employee,
        'data':data,
        'search_form':search_form,
    }
    return render(request, 'admin/product_manager/comments/search_comment.html',context)

# ------------------------------------------ End Admin Page ----------------------------------------------------

# ------------------------------------------ Begin RestAPI ----------------------------------------------------

#                           -------------------- Category -----------------------

# RestAPI Category
class  Category_API_View(APIView):
    def get(self,request):
        listCategory= Category.objects.all()
        Categorydata= CategorySerializer(listCategory, many=True).data # Adding .data to convert the data from ListSerializer to JSON
        return Response(data= Categorydata, status=status.HTTP_200_OK)

#                           -------------------- Product -----------------------

# RestAPI  Product
class Product_API_View(APIView):
    def get(self,request):
        listProduct= Product.objects.all()
        Productdata= ProductSerializer(listProduct, many=True).data # Adding .data to convert the data from ListSerializer to JSON
        return Response(data= Productdata, status=status.HTTP_200_OK)
    # def post(self,request):
    #    Productdata=ProductCreationSerializer(data=request.data)
        
    #     if(not Productdata.is_valid()):
    #         return Response('Dữ liệu bị sai !', status=status.HTTP_400_BAD_REQUEST)

#                           -------------------- Comment -----------------------

# RestAPI Comment
class  Comment_API_View(APIView):
    def get(self,request):
        listComment= Comment.objects.all()
        Commentdata= CommentSerializer(listComment, many=True).data # Adding .data to convert the data from ListSerializer to JSON
        return Response(data= Commentdata, status=status.HTTP_200_OK)
    
# ------------------------------------------ End RestAPI ----------------------------------------------------