from django.contrib import admin

class LaunchAdmin(admin.ModelAdmin):
    list_display = ['flight_number', 'name', 'rocket', 'significant', 'success']
    ordering = ('-flight_number',)
    list_filter = ('date_local', 'significant', 'success', 'upcoming', 'rocket')
