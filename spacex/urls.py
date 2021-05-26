from django.urls import path

from . import views

app_name = 'spacex'
urlpatterns = [
    # ex: launchpads/5/
    path('launchpads/<str:sanitized_name>/', views.launchpad.detail, name='detail'),
]