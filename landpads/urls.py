from django.urls import path

from . import views

app_name = 'landpads'
urlpatterns = [
    # ex: landpads/LZ-2/
    path('<str:id>/', views.detail, name='detail'),
]