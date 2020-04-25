from django.urls import path, include
from . import views
from signup import views as v
urlpatterns = [
    path('', views.home, name='home'),
    path('shelter/', views.shelter, name='shelter'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('signup/', v.signup, name='signup'),
    path('login/', v.login_view, name='login'),
]