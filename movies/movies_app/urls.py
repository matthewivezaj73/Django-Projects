from django.urls import path, include
from movies_app.views import movie_list
urlpatterns = [
    path('list/', movie_list),
]
