from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

def index(request):    
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html' )
    


