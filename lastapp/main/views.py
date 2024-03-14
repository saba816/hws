from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'title': 'Home page',
        'values': ['Sum','Hello','123'],
        'obj': {
            'car': 'Audi',
            'age': 16,
            'hobby': 'football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')