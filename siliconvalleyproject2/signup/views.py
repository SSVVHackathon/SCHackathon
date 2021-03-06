from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from . forms import ProfileForm
from . jsonconversion import conversion
import json
from . forms import ProfileForm, AccountAuthenticationForm
from . getdata import data
from geopy import geocoders

# from .forms import ProfileForm
# Create your views here.
g = geocoders.Nominatim()

def signup(request):
    context = {}
    if request.POST:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            company_name = form.cleaned_data.get('company_name')
            raw_password = form.cleaned_data.get('password1')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            shelter_or_restaurant = form.cleaned_data.get('shelter_or_restaurant')
            shelter_or_restaurant = str(shelter_or_restaurant)
            company_name = str(company_name)
            address = str(address)
            email = str(email)
            thing = g.geocode(address)
            lat, lng = thing.latitude, thing.longitude
            account = authenticate(company_name=company_name, password=raw_password)
            conversion(lat, lng, email, company_name, shelter_or_restaurant, address)
            with open('templates/blah.json') as f:
                information = json.load(f)
            return render(request, 'maps.html', information)
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
                return render(request, 'maps.html')
    else:
        form = AccountAuthenticationForm()
    context['form'] = form
    return render(request, 'login.html', context)