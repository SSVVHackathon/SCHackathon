from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def shelter(request):
    return render(request, 'shelter.html')

def restaurant(request):
    return render(request, 'restaurant.html')