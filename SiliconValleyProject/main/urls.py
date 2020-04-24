from django.urls import path, include
from . import views
from signup import views as v
urlpatterns = [
    path('', views.home, name='home'),
    path('shelter/', views.shelter, name='shelter'),
    path('restaurant/', views.restaurant,name='restaurant'),
    # path('admin/', admin.site.urls),
    path('restaurant/signup', v.signup, name='restaurantsignup'),
]