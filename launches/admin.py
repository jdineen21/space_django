from django.contrib import admin

from .models import Launch

class LaunchAdmin(admin.ModelAdmin):
    list_display = ['flight_number', 'name', 'success']
    ordering = ('-flight_number',)
    list_filter = ('success', 'upcoming', 'tbd')

admin.site.register(Launch, LaunchAdmin)