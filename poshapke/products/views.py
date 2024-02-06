from django.views.generic import ListView, TemplateView

from common.mixins import TitleMixin
from products.models import Category, Products


class IndexView(TitleMixin, TemplateView):
    """
    Главная Страница.
    """
    template_name = 'products/index.html'
    title = 'Главная Страница'


class ProductsListView(TitleMixin, ListView):
    """
    Раздел с Товаром.
    """
    model = Products
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Каталог'

    def get_queryset(self):
        product = super(ProductsListView, self).get_queryset()
        slug = self.kwargs.get('slug')
        return product.filter(category__slug=slug) if slug else product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
