from django.shortcuts import render
from products.models import *

# Create your views here.

def index(request):
    main_categories = MainCategory.objects.all().order_by('title')
    sub_categories = SubCategory.objects.all().order_by('title')
    products = Product.objects.all()

    return render(request, 'index.html', locals())

def mainCategory(request, url):
    mainCategories = MainCategory.objects.filter(slug=url)
    main_categories = MainCategory.objects.all().order_by('title')
    sub_categories = SubCategory.objects.all().order_by('title')

    return render(request, 'main.html', locals())

def subCategory(request, mainurl, suburl):
    subCategories = Product.objects.filter(sub_category__slug=suburl, sub_category__main_category__slug=mainurl)
    main_categories = MainCategory.objects.all().order_by('title')
    sub_categories = SubCategory.objects.all().order_by('title')

    return render(request, 'sub.html', locals())

def detail(request, url):
    val = Product.objects.get(slug=url)

    return render(request, 'product_details.html', locals())


