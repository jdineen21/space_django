from django.urls import path

from . import views

app_name = 'spacex'
urlpatterns = [
    # ex: /
    path('', views.home.index, name='home.index'),
    # ex: /about/
    path('about/', views.home.about, name='home.about'),

    # ex: launches/
    path('launches/', views.launch.index, name='launch.index'),
    # ex: launches/5/
    path('launches/<int:flight_number>/', views.launch.detail, name='launch.detail'),
    # ex: launches/next/
    path('launches/next/', views.launch.next, name='launch.next'),
    # ex: launches/past/
    path('launches/past/', views.launch.past, name='launch.past'),
    # ex: launches/upcoming/
    path('launches/upcoming/', views.launch.upcoming, name='launch.upcoming'),

    # ex: launchpads/5/
    path('launchpads/<str:sanitized_name>/', views.launchpad.detail, name='launchpad.detail'),

    # ex: rockets/falcon9/
    path('rockets/<str:sanitized_name>/', views.rocket.detail, name='rocket.detail'),
]