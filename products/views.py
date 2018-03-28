from django.shortcuts import render
from products.models import *

# Create your views here.

def index(request):
    main_categories = MainCategory.objects.all()
    sub_categories = SubCategory.objects.all()
    products = Product.objects.all()

    return render(request, 'index.html', locals())
