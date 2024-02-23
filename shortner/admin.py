from django.contrib import admin
from .models import  Url # Url is my model
# Register your models here.

# registring the table in the database!
admin.site.register(Url)