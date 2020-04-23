from django.shortcuts import render, redirect
from . forms import RegisterForm
# Create your views here.
def signup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = response.user
            post.save()
        # return redirect('')
    else:
        form = RegisterForm()
    return render(response, 'signup.html', {'form' : form})