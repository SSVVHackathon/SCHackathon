from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from signup.models import Profile

class ProfileForm(UserCreationForm):
    TYPES = (
        ('Shelter', 'Shelter'),
        ('Restaurant', 'Restaurant'),
    )
    email = forms.EmailField(max_length=60, help_text='Required. Add an email address')
    address = forms.CharField(max_length=100, help_text='Required. Add an address')
    company_name = forms.CharField(max_length=100, help_text='Required. Add a company name')
    shelter_or_restaurant = forms.ChoiceField(choices=TYPES)

    class Meta:
        model = Profile
        fields = ("company_name", "email", "password1", "password2", "address", "shelter_or_restaurant")

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('company_name', 'password')
    
    def clean(self):
        if self.is_valid():
            company_name = self.cleaned_data['company_name']
            password = self.cleaned_data['password']
            if not authenticate(company_name=company_name, password=password):
                raise forms.ValidationError("Invalid Login")