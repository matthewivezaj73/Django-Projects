#Importing models.
from django.db import models

# Create your models here.
#Creating a class.
class Movie(models.Model):
    name = models.CharField(max_length=50)