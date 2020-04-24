from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TYPES = [
        ('Shelter', 'Shelter'),
        ('Restaurant', 'Restaurant')
    ]
    email = models.EmailField()
    address = models.CharField(max_length=500)
    types = models.CharField(max_length=500)
# class AdressField(models.Models):
