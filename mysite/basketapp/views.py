from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Basket
from mainapp.models import CollectionsImg

def basket(request):
    content = {}
    return render(request, 'basketapp/basket.html', content)

def basket_add(request, pk):
    product = get_object_or_404(CollectionsImg, pk=pk)
    old_basket_item = Basket.object.filter(user=request.user, product=product)

    if old_basket_item:
        old_basket_item[0].basket_quantity += 1
        old_basket_item[0].save()
    else:
        new_basket_item = Basket(user=request.user, product=product)
        new_basket_item.basket_quantity += 1
        new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_remove(request, pk):
    content = {'pk': pk}
    return render(request, 'basketapp/basket.html', content)