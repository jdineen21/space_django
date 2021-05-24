from django.contrib import admin

from .models import Launch

class LaunchAdmin(admin.ModelAdmin):
    list_display = ['flight_number', 'name', 'rocket', 'success']
    ordering = ('-flight_number',)
    list_filter = ('date_local', 'success', 'upcoming', 'rocket')

admin.site.register(Launch, LaunchAdmin)