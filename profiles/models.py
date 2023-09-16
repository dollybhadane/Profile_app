from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile_photos/')
    description = models.TextField()
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()