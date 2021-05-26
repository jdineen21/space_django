from django.urls import path

from . import views

app_name = 'spacex'
urlpatterns = [
    # ex: launches/
    path('launches/', views.launch.index, name='index'),
    # ex: launches/5/
    path('launches/<int:flight_number>/', views.launch.detail, name='detail'),
    # ex: launches/next/
    path('launches/next/', views.launch.next, name='next'),
    # ex: launches/past/
    path('launches/past/', views.launch.past, name='past'),
    # ex: launches/upcoming/
    path('launches/upcoming/', views.launch.upcoming, name='upcoming'),

    # ex: launchpads/5/
    path('launchpads/<str:sanitized_name>/', views.launchpad.detail, name='detail'),

    # ex: rockets/falcon9/
    path('rockets/<str:rocket_id>/', views.rocket.detail, name='detail'),
]