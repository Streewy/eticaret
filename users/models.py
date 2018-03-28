from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from products.models import Product

# Create your models here.

class User(AbstractUser):
    """
    This class will be our user model.
    """
    adres = models.CharField(max_length=255, null=True, blank=True)
    tel = models.CharField(max_length=255, null=True, blank=True)