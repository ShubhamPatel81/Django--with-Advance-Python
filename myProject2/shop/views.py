# views.py
from django.shortcuts import render

def product_view(request):
    return render(request, 'shop/product.html')