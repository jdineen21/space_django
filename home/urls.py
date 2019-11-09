from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /contact/
    path('contact/', views.contact, name='contact'),
]