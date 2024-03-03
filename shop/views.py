from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("contact")

def tracker(request):
    return HttpResponse("tracker")

def prodView(request):
    return HttpResponse("Product View")

def search(request):
    return HttpResponse("Search")

def checkout(request):
    return HttpResponse("Checkout")

