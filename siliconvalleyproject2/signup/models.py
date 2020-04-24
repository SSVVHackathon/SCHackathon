from django.db import models

# Create your models here.
class Profile(models.Model):
    company_name = models.CharField(max_length=500)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    address = models.CharField(max_length=500)