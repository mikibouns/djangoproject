from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Basket
from mainapp.models import Collections
from mainapp.views import basket_func, wallpaper_collections

def basket(request):
    title = 'basket'
    content = {'basket': basket_func(request),
               'title': title,
               'collections': wallpaper_collections}
    return render(request, 'basketapp/basket.html', content)

def basket_add(request, pk):
    product = get_object_or_404(Collections, pk=pk)
    print(product)
    old_basket_item = Basket.objects.filter(basket_user=request.user, basket_product=product)

    if old_basket_item:
        old_basket_item[0].basket_quantity += 1
        old_basket_item[0].save()
    else:
        new_basket_item = Basket(basket_user=request.user, basket_product=product)
        new_basket_item.basket_quantity += 1
        new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))