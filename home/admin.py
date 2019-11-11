from django.contrib import admin

from .models import SignificantLaunch

class SignificantLaunchAdmin(admin.ModelAdmin):
    list_display = ['flight_number']

admin.site.register(SignificantLaunch, SignificantLaunchAdmin)
