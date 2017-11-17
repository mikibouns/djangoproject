from django.shortcuts import render, render_to_response

def main(request):
    return render_to_response('index.html')

def contacts(request):
    return render_to_response('contacts.html')

def collections(request):
    return render_to_response('collections.html')

