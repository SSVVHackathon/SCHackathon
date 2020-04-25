from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from . forms import ProfileForm
import json
# from .forms import ProfileForm
# Create your views here.

def signup(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data.get('address'))
        # data = {
        #     "address":f"{form.cleaned_data.get('address')}",
        #     "company_name":f'{form.cleaned_data.get("company_name")}',
        #     "email":f'{form.cleaned_data.get("email")}'
        # }
        # with open('sign_up_data.json','w') as j:
        #     file_data = json.load(j)
        #     file_data['companies'].append(data)
        #     json.dump(file_data,j)
        form.save()
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
            context['form'] = form
    else:
        form = ProfileForm()
        context['form'] = form
    return render(request, 'signup.html', context)


