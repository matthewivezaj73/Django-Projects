#importing the render.
from django.shortcuts import render
#Importing the application.
from movies_app.models import Movie
#Importing json response.
from django.http import JsonResponse
# Create your views here.
#Creating a function to handle requests.
def movie_list(request):
    #Creating a query set of all objects.
    movies = Movie.objects.all()
    #Creating a dictionary.
    # data = {
    #     'movies': list(movies.values)
    # }
    #Returning the json response.
    return JsonResponse()