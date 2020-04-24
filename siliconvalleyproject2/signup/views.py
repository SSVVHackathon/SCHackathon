from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# from .forms import ProfileForm
# Create your views here.

def signup(request):
    return render(request, 'signup.html', {'form':'HI'})
