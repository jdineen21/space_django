from django.urls import path

from . import views

app_name = 'spacex'
urlpatterns = [
    # ex: /
    path('', views.home.index, name='home.index'),
    # ex: /about/
    path('about/', views.home.about, name='home.about'),

    # ex: cores/5/
    path('cores/<str:serial>/', views.core.detail, name='core.detail'),

    # ex: dragons/dragon-1/
    path('dragons/<str:sanitized_name>/', views.dragon.detail, name='dragon.detail'),

    # ex: landpads/lz-2/
    path('landpads/<str:sanitized_name>/', views.landpad.detail, name='landpad.detail'),

    # ex: launches/
    path('launches/', views.launch.index, name='launch.index'),
    # ex: launches/5/
    path('launches/<int:page_number>/', views.launch.detail, name='launch.detail'),
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