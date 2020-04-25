from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse
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
        form = ProfileForm()
    return render(request, "signup.html", {'form':form})
