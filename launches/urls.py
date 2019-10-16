from django.urls import path

from . import views

app_name = 'launches'
urlpatterns = [
    # ex: launches/
    path('', views.index, name='index'),
    # ex: launches/upcoming
    path('upcoming/', views.upcoming, name='upcoming'),
]