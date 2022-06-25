from django.urls import path, include
from movies_app.views import movie_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('movies_app.urls')),
]