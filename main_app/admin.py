from django.contrib import admin
# import your models here
from .models import Card, Cleaning
# Register your models here
admin.site.register([Card, Cleaning])
