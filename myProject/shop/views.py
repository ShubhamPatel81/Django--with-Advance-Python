from django.shortcuts import render 

from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to the myProject Shop home page!</h1>");
def product(request):
    
    return HttpResponse(f"<h1>Welcome to the myProject Shop product page!</h1> <p>This is a simple product page.</p>" );