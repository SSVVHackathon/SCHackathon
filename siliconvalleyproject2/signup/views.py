from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from . forms import ProfileForm
# from .forms import ProfileForm
# Create your views here.

def signup(request):
    context = {}
    if request.POST:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            company_name = form.cleaned_data.get('company_name')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(company_name=company_name, password=raw_password)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = ProfileForm()
        context['registration_form'] = form
    return render(request, 'signup.html', context)


