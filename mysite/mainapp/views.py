from django.shortcuts import render, render_to_response
from .models import Collections, CollectionsImg

import datetime

current_date = datetime.date.today()
wallpaper_collections = Collections.objects.all().order_by('collection_name')


def main(request):
    return render(request, 'index.html', {'current_date': current_date, 'collections': wallpaper_collections})


def contacts(request):
    return render(request, 'contacts.html', {'collections': wallpaper_collections})


def collections_page(request):
    return render(request, 'collections.html', {'collections': wallpaper_collections})


def product_page(request, collection_name):
    current_collection = Collections.objects.get(collection_name=collection_name)
    current_wallpaper_img = CollectionsImg.objects.filter(img_collection__collection_name=collection_name)
    count_img = range(1, len(current_wallpaper_img) + 1)
    return render(request, 'product_page.html', {'collections': wallpaper_collections,
                                                 'current_collection': current_collection,
                                                 'current_wallpaper_img': current_wallpaper_img,
                                                 'count_img': count_img})
