from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'Стальной Узор',
        'content':'Главная страница студии Стальной Узор',
        'list':['first','second'],
        'dict':{'first': 1},
        'is_authenticated': False
    }
    return render(request,'main/index.html', context )

def about(request):
    return HttpResponse('просто хуй')
