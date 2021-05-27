from django.contrib import admin

class LaunchAdmin(admin.ModelAdmin):
    list_display = ['flight_number', 'name', 'rocket', 'success']
    ordering = ('-flight_number',)
    list_filter = ('date_local', 'success', 'upcoming', 'rocket')

class SignificantLaunchAdmin(admin.ModelAdmin):
    list_display = ['flight_number']
