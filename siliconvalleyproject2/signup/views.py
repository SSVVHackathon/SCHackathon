from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse
from . forms import ProfileForm
# from .forms import ProfileForm
# Create your views here.

def signup(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        form = ProfileForm()

    return render(request, "signup.html", {'form':form})
