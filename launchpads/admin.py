from django.contrib import admin

from .models import LaunchpadImage

class LaunchpadImageAdmin(admin.ModelAdmin):
    list_display = ['site_id', 'image_location']

admin.site.register(LaunchpadImage, LaunchpadImageAdmin)