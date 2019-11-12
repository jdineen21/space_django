from django.urls import path

from . import views

app_name = 'rockets'
urlpatterns = [
    # ex: rockets/falcon9/
    path('<str:rocket_id>/', views.detail, name='detail'),
]