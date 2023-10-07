from django.db import models


class People(models.Model):
    headline = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name


from . models import People

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()

    def __str__(self):
        return self.name

