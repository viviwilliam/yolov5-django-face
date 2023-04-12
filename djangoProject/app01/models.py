import os

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class Photo(models.Model):
    username = models.CharField(max_length=32)
    priPhotoDate = models.CharField(max_length=64)
    photoDate = models.CharField(max_length=64)


