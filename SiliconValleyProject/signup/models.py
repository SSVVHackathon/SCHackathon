from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.
class Signup(models.Model):
    address = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)