from django.urls import path

from . import views

app_name = 'spacex'
urlpatterns = [
    # ex: /spacex/
    path('', views.index, name='index'),
]