from django.urls import path

from . import views

app_name = 'launches'
urlpatterns = [
    # ex: launches/
    path('', views.index, name='index'),
    # ex: launches/5/
    path('<int:flight_number>/', views.detail, name='detail'),
    # ex: launches/next/
    path('next/', views.next, name='next'),
    # ex: launches/past/
    path('past/', views.past, name='past'),
    # ex: launches/upcoming/
    path('upcoming/', views.upcoming, name='upcoming'),
]