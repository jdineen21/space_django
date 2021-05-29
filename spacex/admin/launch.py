from django.contrib import admin

class LaunchAdmin(admin.ModelAdmin):
    search_fields = [
        'flight_number',
        'name',
    ]
    list_display = [
        'flight_number',
        'name', 'rocket',
        'significant',
        'success',
    ]
    ordering = ['-flight_number']
    list_filter = [
        'date_local',
        'significant',
        'success',
        'upcoming',
        'rocket',
    ]
