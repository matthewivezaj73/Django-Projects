from django.urls import path, include

urlpatterns = [
    path('movie/', include(movie_app.urls)),
]
