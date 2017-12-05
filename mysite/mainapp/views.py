from django.shortcuts import render
from .models import Collections, CollectionsImg
from basketapp.models import Basket

import datetime

current_date = datetime.date.today()
wallpaper_collections = Collections.objects.all().order_by('collection_name')

def basket_func(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(basket_user=request.user)
    return basket

def main(request):
    title = 'index'
    content = {'title': title,
               'basket': basket_func(request),
               'collections': wallpaper_collections,
               'current_date': current_date}

    return render(request, 'index.html', content)


def contacts(request):
    title = 'contacts'
    content = {'title': title,
               'basket': basket_func(request),
               'collections': wallpaper_collections}
    return render(request, 'contacts.html', content)


def collections_page(request):
    title = 'collections'
    content = {'title': title,
               'basket': basket_func(request),
               'collections': wallpaper_collections}
    return render(request, 'collections.html', content)


def product_page(request, collection_name):
    title = 'product_page'
    current_collection = Collections.objects.get(collection_name=collection_name)
    current_wallpaper_img = CollectionsImg.objects.filter(img_collection__collection_name=collection_name)
    content = {'title': title,
               'collections': wallpaper_collections,
               'current_collection': current_collection,
               'current_wallpaper_img': current_wallpaper_img,
               'basket': basket_func(request)}
    return render(request, 'product_page.html', content)

