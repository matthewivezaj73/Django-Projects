#importing the render.
from django.shortcuts import render
#Importing the application.
from movies_app.models import Movie
# Create your views here.
#Creating a function.
def movie_list(request):