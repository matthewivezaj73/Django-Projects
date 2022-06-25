#Importing models.
from django.db import models

# Create your models here.
#Creating a class.
class Movie(models.Model):
    # Creating a charfield and assigned it to the variable name.
    name = models.CharField(max_length=50)
    #Creating another charfield and assigned it to the variable description.