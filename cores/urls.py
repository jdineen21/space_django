from django.urls import path

from . import views

app_name = 'cores'
urlpatterns = [
    # ex: cores/
    #path('', views.index, name='index'),
    # ex: cores/5/
    path('<str:core_serial>/', views.detail, name='detail'),
]