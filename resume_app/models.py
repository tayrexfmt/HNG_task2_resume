from django.db import models

# Create your models here.
class feature(models.Model):
    #id: int
    usernamename = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    phonenumber = models.IntegerField(max_length=15)
    address = models.CharField(max_length=500)
    comment = models.CharField(max_length=500)
    