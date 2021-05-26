from django.contrib import admin

from spacex.models import LaunchpadImage

class LaunchpadImageInline(admin.StackedInline):
    model = LaunchpadImage
    list_display = ['site_id', 'image_location']

class LaunchpadAdmin(admin.ModelAdmin):
    inlines = [LaunchpadImageInline]
