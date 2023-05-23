import sys
sys.path.append("..")
from django.shortcuts import render
from utils import get_db_handle
#from django.http import HttpResponse

# Create your views here.

context ={
        "data":"Contact Me",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }

def index(request):
    
    return render(request, 'index.html')

def about(request):
    
    return render(request, 'about.html')

def contact(request):
    print(get_db_handle('127.0.0.1', 27017, context))
    print('Inside Contact')
    #collection.insert_one(context)
    return render(request, 'contact.html', context)

# get_db_handle('127.0.0.1', 27017)