from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView

from products.models import Category, Products


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Главная Страница'
        return context


def products(request, slug=None):
    per_page = 3
    product = Products.objects.filter(
        category__slug=slug) if slug else Products.objects.all()
    paginator = Paginator(product, per_page=per_page)
    page = request.GET.get('page', 1)
    page_products = paginator.page(page)

    context = {
        'title': 'Товары',
        'categories': Category.objects.all(),
        'products': page_products,
    }
    return render(request, template_name='products/products.html',
                  context=context)
