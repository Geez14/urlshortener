from django.db import models
# Create your models here.

# url table and column is link and uuid
MAXLENGTH_UUID = 7

class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=MAXLENGTH_UUID)


class Api_Keys(models.Model):
    api_key = models.CharField(max_length=64, primary_key = True)