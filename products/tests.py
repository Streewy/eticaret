from django.test import TestCase
from products.models import *

# Create your tests here.

class MainTestCase(TestCase):
    def setUp(self):
        MainCategory.objects.create(title='IOS')

    def testMainCategory(self):
        i = MainCategory.objects.get(title='IOS')
        self.assertEquals(i.title,'OSMAN')