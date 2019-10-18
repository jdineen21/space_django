from django.urls import path

from . import views

app_name = 'cores'
urlpatterns = [
    # ex: cores/
    #path('', views.index, name='index'),
    # ex: cores/5/
    path('<str:site_id>/', views.detail, name='detail'),
]