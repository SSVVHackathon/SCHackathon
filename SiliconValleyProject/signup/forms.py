from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    address = forms.CharField(max_length=500)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]