from django.urls import path

from . import views

app_name = 'dragons'
urlpatterns = [
    # ex: dragons/dragon1/
    path('<str:id>/', views.detail, name='detail'),
]