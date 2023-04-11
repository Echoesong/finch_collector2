from django.shortcuts import render

finches = [ 
    {'name': 'Red',
     'color': 'Red',
     'fav color': 'Red'},

     {'name': 'Blue',
     'color': 'Blue',
     'fav color': 'Blue'},

     {'name': 'Purple',
     'color': 'Purple',
     'fav color': 'Purple'}]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')