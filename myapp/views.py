import sys
sys.path.append("..")
from django.template.loader import render_to_string
from django.shortcuts import render
from utils import get_db_handle
from .models import blog, item

# Create your views here.

func_data = get_db_handle('127.0.0.1', 27017)

contact_details = func_data['webpageinfo'].find_one({"_id" : 1})

about_details = func_data['webpageinfo'].find_one({"_id" : 2})

home_details = func_data['webpageinfo'].find_one({"_id" : 3})

def index(request):
    
    print("-----------------------HOME-----------------------\n")
    blogs = blog.objects.all()
    items = item.objects.all()
    print(blogs, items)
    return render(request, 'index.html', {'blogs': blogs})

def about(request):
    
    print("-----------------------ABOUT-----------------------\n", about_details)
    return render(request, 'about.html', about_details)

def contact(request):
    
    print("-----------------------Contact Me-----------------------\n", contact_details)
    #rendering the data from mongoDb
    return render(request, 'contact.html', contact_details)

def post(request, pk):

    posts = blog.objects.get(id=pk)
    print("-----------------------Post.html---------------------------\n", posts.id)
    return render(request, 'post.html', {'posts': posts})