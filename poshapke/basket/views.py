from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from basket.models import Basket
from products.models import Products


def basket_add(request, slug):
    user = request.user
    product = get_object_or_404(Products, slug=slug)
    baskets = Basket.objects.filter(user=user, product=product)
    if baskets.exists():
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    Basket.objects.create(user=user, product=product, quantity=1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
