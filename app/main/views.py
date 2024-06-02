from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

def index(request):
    context : dict[str,str] = {
        'title': 'Home',
        'content' : 'Главная страница'
    }
    
    return render(request, 'main/index.html',context)


def about(request):
    return render(request, 'main/about.html',context)