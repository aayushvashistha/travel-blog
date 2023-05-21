from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

context ={
        "data":"Contact Me",
        #"list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }

def index(request):
    
    return render(request, 'index.html')

def about(request):
    
    return render(request, 'about.html')

def contact(request):
    
    return render(request, 'contact.html', context)