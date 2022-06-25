#Importing models.
from django.db import models

# Create your models here.
#Creating a class.
class Movie(models.Model):
    # Creating a charfield and assigned it to the variable name.
    name = models.CharField(max_length=50)
    #Creating another charfield and assigned it to the variable description.
    description = models.CharField(max_length=200)
    #Creating a Booleanfield and assigned it to the variable active.
    active = models.BooleanField(default=True)
    
    def __str__(self):
        """
            Returning the name of the model.
        """
        #Returning the name of the model.