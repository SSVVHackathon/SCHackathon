from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from . forms import ProfileForm
from . jsonconversion import conversion
import json
from . forms import ProfileForm, AccountAuthenticationForm
# from .forms import ProfileForm
# Create your views here.

def signup(request):
    context = {}
    if request.POST:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            company_name = form.cleaned_data['company_name']
            raw_password = form.cleaned_data['password1']
            # address = form.cleaned_data['address']
            # email = form.cleaned_data['email']
            # conversion(address,email,company_name)
            account = authenticate(company_name=company_name, password=raw_password)
            return redirect('home')
        else:
            context['form'] = form
    else:
        form = ProfileForm()
        context['form'] = form
    return render(request, 'signup.html', context)

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            company_name = request.POST['company_name']
            password = request.POST['password']
            user = authenticate(company_name=company_name, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()
    context['form'] = form
    return render(request, 'login.html', context)
