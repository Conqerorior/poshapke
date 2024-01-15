from django.shortcuts import render

from basket.models import Basket
from products.models import Category, Products


def index(request):
    return render(request=request, template_name='products/index.html')


def products(request):
    context = {
        'title': 'Товары',
        'categories': Category.objects.all(),
        'products': Products.objects.all(),
    }
    return render(request, template_name='products/products.html',
                  context=context)
