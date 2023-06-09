import sys
sys.path.append("..")
from django.template.loader import render_to_string
from django.shortcuts import render
from utils import get_db_handle
from .models import blog, item

# Create your views here.

# func_data = get_db_handle('127.0.0.1', 27017)

# contact_details = func_data['webpageinfo'].find_one({"_id" : 1})

# about_details = func_data['webpageinfo'].find_one({"_id" : 2})

# home_details = func_data['webpageinfo'].find_one({"_id" : 3})

def index(request):
    
    print("-----------------------HOME-----------------------\n")
    blogs = blog.objects.all()
    items = item.objects.filter(heading='Welcome')
    print(blogs, items)
    return render(request, 'index.html', {'blogs': blogs, 'items': items})

def about(request):
    
    print("-----------------------ABOUT-----------------------\n")
    items = item.objects.filter(heading='About Me')
    return render(request, 'about.html', {'items': items})

def contact(request):
    
    print("-----------------------Contact Me-----------------------\n")
    items = item.objects.filter(heading='Contact Me')
    return render(request, 'contact.html', {'items': items})

def post(request, pk):

    posts = blog.objects.get(id=pk)
    print("-----------------------Post.html---------------------------\n", posts.id)
    return render(request, 'post.html', {'posts': posts})