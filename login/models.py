from django.db import models

# Create your models here.

class test_login(models.Model):
    lo_name=models.CharField(max_length=30,unique=True)
    lo_pwd=models.CharField(max_length=30)