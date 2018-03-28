import django.contrib

from django.contrib import admin
from products.models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}



django.contrib.admin.site.register(Product, ProductAdmin)
django.contrib.admin.site.register(MainCategory, ProductAdmin)
django.contrib.admin.site.register(SubCategory, ProductAdmin)