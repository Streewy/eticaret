from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MainCategory(models.Model):

    title = models.CharField(max_length=255, null=False, blank=False, help_text="Bu alan bos birakilamaz!")
    image = models.ImageField(upload_to='media/urun_resimleri/%Y/%m/%d', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=80, null=True, help_text=u"Link, otomatik alinir. Degistirmeyiniz!")
    enable = models.BooleanField(default=True)

    def __unicode__(self):
        return '{}'.format(self.title)

class SubCategory(models.Model):

    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name="main_category")
    title = models.CharField(max_length=255, null=False, blank=False, help_text="Bu alan bos birakilamaz!")
    image = models.ImageField(upload_to='media/urun_resimleri/%Y/%m/%d', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=80, null=True, help_text=u"Link, otomatik alinir. Degistirmeyiniz!")
    enable = models.BooleanField(default=True)

    def __unicode__(self):
        return '{}'.format(self.title)

class Product(models.Model):

    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="sub_category")
    title = models.CharField(max_length=255, null=False, blank=False, help_text="Bu alan bos birakilamaz!")
    price = models.CharField(max_length=255, null=False, blank=False, help_text="Fiyat bos birakilamaz!")
    image = models.ImageField(upload_to='media/urun_resimleri/%Y/%m/%d', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    definition = models.TextField(null = True, blank=True, help_text="Urunun aciklamasini giriniz!")
    slug = models.SlugField(max_length=80, null=True, help_text=u"Link, otomatik alinir. Degistirmeyiniz!")
    viewCount = models.IntegerField(default=0, editable=False)
    enable = models.BooleanField(default=True)

    def __unicode__(self):
        return '{}'.format(self.title)

