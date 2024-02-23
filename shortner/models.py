from django.db import models
# Create your models here.

# url table and column is link and uuid
MAXLENGTH_UUID = 5

class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=MAXLENGTH_UUID)