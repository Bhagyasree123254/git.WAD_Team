from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category



def Home(request):
    products = None
    categories = Category.get_all_categories()
    catgoryID= request.GET.get('category')
    if catgoryID:
        products = Product.get_all_products_by_id(catgoryID)
    else:
        products = Product.get_all_products();

    data= {products: products, categories: categories}
    return render(request, 'Home.html', {'categories': categories})



def category(request):
    products = None
    categories = Category.get_all_categories()
    catgoryID = request.GET.get('category')
    if catgoryID:
        products = Product.get_all_products_by_id(catgoryID)
    else:
        products = Product.get_all_products();

    data = {products: products, categories: categories}


    return render(request, 'category.html', {'products':products})


def bookpage(request):
    name=request.GET.get('name')
    if name:
        products = Product.get_products_by_name(name)
    else:
        products = Product.get_all_products();

    return render(request,'bookpage.html',{'products': products})


def booksdownload(request):
    products=Product.get_all_products()
    return render(request,'booksdownload.html',{'products':products})