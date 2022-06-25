from django.urls import path

urlpatterns = [
    path('movie/', include(movie_app.urls)),
]
