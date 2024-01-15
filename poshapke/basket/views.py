from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from basket.models import Basket
from products.models import Products


@login_required
def basket_add(request, slug):
    user = request.user
    product = get_object_or_404(Products, slug=slug)
    baskets = Basket.objects.filter(user=user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, basket_id):
    basket = get_object_or_404(Basket, id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
