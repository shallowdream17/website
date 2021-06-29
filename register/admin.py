from django.contrib import admin

# Register your models here.
from .models import test_register
admin.site.register(test_register)
