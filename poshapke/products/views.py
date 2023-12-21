from django.shortcuts import render

from products.models import Category


def index(request):
    return render(request=request, template_name='products/index.html')


def products(request):
    context = {
        'title': 'Товары',
        'categories': Category.objects.all()
    }
    return render(request, template_name='products/products.html', context=context)
