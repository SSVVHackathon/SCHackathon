from django.db import models

# Create your models here.
class Restaurant(models.Model):
    STATUS = (
        ('GIVING', 'GIVING'),
        ('NOTGIVING', 'NOTGIVING')
    )


    name = models.CharField(max_length=500, null=True)
    email = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.name
