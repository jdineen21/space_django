from django.urls import path

from . import views

app_name = 'spacex'
urlpatterns = [
    # ex: rockets/falcon9/
    path('rockets/<str:rocket_id>/', views.detail, name='detail'),
]