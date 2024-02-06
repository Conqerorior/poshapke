from .models import Basket


def baskets(request):
    if request.user.is_authenticated:
        return {'baskets': Basket.objects.filter(user=request.user)}
    return {'baskets': []}
