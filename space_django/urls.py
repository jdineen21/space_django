"""space_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'space-track.com Admin'
admin.site.site_title = 'space-track.com Admin Portal'
admin.site.index_title = 'Welcome to the space-track.com Admin Portal'

urlpatterns = [
    #path('', include('home.urls')),
    #path('cores/', include('cores.urls')),
    #path('landpads/', include('landpads.urls')),
    path('', include('spacex.urls')),
    #path('launchpads/', include('launchpads.urls')),
    #path('rockets/', include('rockets.urls')),
    #path('dragons/', include('dragons.urls')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
