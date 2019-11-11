from django.urls import path

from . import views

app_name = 'launchpads'
urlpatterns = [
    # ex: launchpads/5/
    path('<str:site_id>/', views.detail, name='detail'),
]