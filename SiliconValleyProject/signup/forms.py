from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Signup

class RegisterForm(forms.ModelForm):
    address = forms.CharField(max_length=500)
    class Meta:
        model = Signup
        fields = ('address',)