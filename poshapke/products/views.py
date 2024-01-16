from django.views.generic import TemplateView, ListView

from products.models import Category, Products


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Главная Страница'
        return context


class ProductsListView(ListView):
    model = Products
    template_name = 'products/products.html'
    paginate_by = 3

    def get_queryset(self):
        product = super(ProductsListView, self).get_queryset()
        slug = self.kwargs.get('slug')
        return product.filter(category__slug=slug) if slug else product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['title'] = 'Каталог'
        context['categories'] = Category.objects.all()
        return context

# def products(request, slug=None):
#     per_page = 3
#     product = Products.objects.filter(
#         category__slug=slug) if slug else Products.objects.all()
#     paginator = Paginator(product, per_page=per_page)
#     page = request.GET.get('page', 1)
#     page_products = paginator.page(page)
#
#     context = {
#         'title': 'Товары',
#         'categories': Category.objects.all(),
#         'products': page_products,
#     }
#     return render(request, template_name='products/products.html',
#                   context=context)
