from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'home.html',{'title':'FWISB Home','homepage':'true','heading':'Food Where It Should Be'})

def shelter(request):
    return render(request, 'shelter.html', {'title':"FWISB Shelter",'heading':'Shelter'})

def restaurant(request):
    return render(request, 'restaurant.html',{'title':"FWISB Restaurant",'heading':'Restaurant'})