from django.shortcuts import render

from products.models import Category, Products


def index(request):
    return render(request=request, template_name='products/index.html')


def products(request, slug=None):
    product = Products.objects.filter(
        category__slug=slug) if slug else Products.objects.all()

    context = {
        'title': 'Товары',
        'categories': Category.objects.all(),
        'products': product,
    }
    return render(request, template_name='products/products.html',
                  context=context)
