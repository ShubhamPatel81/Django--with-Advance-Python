from django.shortcuts import render
from datetime import datetime


# Create your views here.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def home(request):
    context={
        'name': 'John Doe',
        'age': 24,
        "skill":["Python","Django","JavaScript"],
        'user': User('Alice', 25)
        ,
        "blog":{
            "title": "My Blog First Post",
            "content": "<b>Welcome to my blog!</b> This is my first post.",
          "created_at": datetime.now()
        }
        ,
        "empty_value": None,
    }
    return render(request,"blog/home.html",context)