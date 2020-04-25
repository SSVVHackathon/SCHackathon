from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('shelter/', views.shelter, name='shelter'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('restaurant/signup', include('signup.urls')),
]