from django.shortcuts import render

finches = [ 
    {'name': 'Red',
     'color': 'Red',
     'fav_color': 'Red'},

     {'name': 'Blue',
     'color': 'Blue',
     'fav_color': 'Blue'},

     {'name': 'Purple',
     'color': 'Purple',
     'fav_color': 'Purple'}]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })