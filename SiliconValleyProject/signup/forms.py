from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import *

class ProfileForm(UserCreationForm):
    TYPES = [
        ('Shelter', 'Shelter'),
        ('Restaurant', 'Restaurant')
    ]
    email = forms.EmailField(required=True)
    address = forms.CharField()
    types = forms.ChoiceField(choices=TYPES)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "address", "types")

    # def save(self, commit=True):
    #     user = super(ProfileForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     user.address = self.cleaned_data["address"]
    #     user.types = self.cleaned_data["types"]
    #     if commit:
    #         user.save()
    #     return user
