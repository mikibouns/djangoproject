from django.shortcuts import render, render_to_response
import json, os
import datetime

current_date = datetime.date.today()

def main(request):
    return render(request, 'index.html', {'current_date': current_date})

def contacts(request):
    return render(request, 'contacts.html')

def collections(request):
    with open(os.path.join(os.getcwd(), 'static/json/base.json'), encoding='utf-8') as file:
        collections = json.load(file)
    return render(request, 'collections.html', {'collections': collections})

