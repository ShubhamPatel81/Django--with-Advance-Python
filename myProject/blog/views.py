from django.shortcuts import render 

from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to the myProject blog home page!</h1>");
def about(request):
    a = 10
    b = 30
    c = a + b
    return HttpResponse(f"<h1>Welcome to the myProject blog about page!</h1> <p>The sum of a and b is: {c}</p>" );

def post_details(request, post_id):
    return HttpResponse(f"<h1>Details of Post ID: {post_id}</h1>");

def user_profile(request, username):
    return HttpResponse(f"<h1>User Profile: {username}</h1>");

def articles(request, year):
    return HttpResponse(f"<h1>Details of Article (Year): {year}</h1>");


# def article_details(request, year,month):
#     return HttpResponse(f"<h1>Details of Article (Year: {year}, Month: {month})</h1>");

def article_details(request, **kwargs):
    
    return HttpResponse(f"<h1>Details of Article : {kwargs}</h1>");