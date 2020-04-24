from django import forms
from . models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['company_name', 'email', 'password', 'address']