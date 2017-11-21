from django.shortcuts import render, render_to_response
import json, os

def main(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')

def collections(request):
    with open(os.path.join(os.getcwd(), 'static/json/base.json'), encoding='utf-8') as file:
        collections = json.load(file)
    return render(request, 'collections.html', {'collections': collections})

