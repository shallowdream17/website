from django.db import models

# Create your models here.

class OAUser(models.Model):
    name=models.CharField(max_length=32,primary_key=True)
    password=models.CharField(max_length=200)
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    is_active=models.CharField(max_length=2)

