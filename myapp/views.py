import sys
sys.path.append("..")
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import forms
from django.db import IntegrityError
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import blog, item, Subscriber, write
from django.urls import reverse

# Create your views here.

# func_data = get_db_handle('127.0.0.1', 27017)

# contact_details = func_data['webpageinfo'].find_one({"_id" : 1})

# about_details = func_data['webpageinfo'].find_one({"_id" : 2})

# home_details = func_data['webpageinfo'].find_one({"_id" : 3})

# @login_required
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

def login(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def subscribe(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, "Thank you for subscribing!" )
            return redirect('index')  # Redirect to a success page
    except IntegrityError as e:
        e = "You are already subscribed"
        messages.error(request, e)
        return redirect("index")
    # messages.error(request, "Error in subscribing")
    # return render(request, 'contact.html')

def writeToUs(request):
    try:
        if request.method == 'POST':
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            message = request.POST.get('message')
            print(email)
            data = write.objects.create(fullname=fullname,email=email,message=message)
            # data.save()
            messages.success(request, "Thanks for sending us a message. We will reach out to you shortly!" )
            return redirect('contact')  # Redirect to a success page
    except:
        return redirect("index")