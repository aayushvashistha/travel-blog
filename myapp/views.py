import sys
sys.path.append("..")
from django.template.loader import render_to_string
from django.shortcuts import render
from utils import get_db_handle
#from django.http import HttpResponse

# Create your views here.
# fun_data = {}

# context ={
#         "data":"Contact Me",
#         # "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     }
fun_data = get_db_handle('127.0.0.1', 27017)

collection = fun_data['newcollection']
op = dict(collection.find_one({}))

def index(request):
    
    return render(request, 'index.html')

def about(request):
    
    return render(request, 'about.html')

def contact(request):
    # fun_data = get_db_handle('127.0.0.1', 27017, context)
    print(op)
    print('Inside Contact')

    #rendering the data from mongoDb
    return render(request, 'contact.html', op)


# get_db_handle('127.0.0.1', 27017)