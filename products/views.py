from django.shortcuts import render
from products.models import *

# Create your views here.

def index(request):
    main_categories = MainCategory.objects.all()
    sub_categories = SubCategory.objects.all()
    products = Product.objects.all()

    return render(request, 'index.html', locals())

def mainCategory(request, url):
    mainCategories = MainCategory.objects.filter(slug=url)

    return render(request, 'main.html', locals())

def subCategory(request, mainurl, suburl):
    subCategories = Product.objects.filter(sub_category__slug=suburl, sub_category__main_category__slug=mainurl)

    return render(request, 'sub.html', locals())

def detail(request, url):
    val = Product.objects.get(slug=url)

    return render(request, 'product_details.html', locals())


