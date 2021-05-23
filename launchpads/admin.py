from django.contrib import admin

from .models import Launchpad, LaunchpadImage

class LaunchpadImageInline(admin.StackedInline):
    model = LaunchpadImage
    list_display = ['site_id', 'image_location']

class LaunchpadAdmin(admin.ModelAdmin):
    inlines = [LaunchpadImageInline]

admin.site.register(Launchpad, LaunchpadAdmin)