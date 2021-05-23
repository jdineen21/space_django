from django.urls import path

from . import views

app_name = 'launchpads'
urlpatterns = [
    # ex: launchpads/5/
    path('<str:sanitized_name>/', views.detail, name='detail'),
]