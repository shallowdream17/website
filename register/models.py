from django.db import models

# Create your models here.

class test_register(models.Model):
    re_name=models.CharField(max_length=30,unique=True)
    re_pwd=models.CharField(max_length=30)