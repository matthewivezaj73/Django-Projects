#importing the render.
from django.shortcuts import render
#Importing the application.
from movies_app.models import Movie
# Create your views here.
#Creating a function to handle requests.
def movie_list(request):
    #Creating a query set of all objects.
    movies = Movie.objects.all()
    #Printing the movies.
    print(movies)