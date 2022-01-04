from django.contrib import admin

from spacex.models import Payload

class PayloadInline(admin.StackedInline):
    model = Payload
    list_display = ['name', 'type']
    extra = 0

class LaunchAdmin(admin.ModelAdmin):
    search_fields = ['flight_number', 'name']
    list_display = ['flight_number', 'name', 'rocket', 'significant', 'success']
    ordering = ['-flight_number']
    list_filter = ['date_local', 'significant', 'success', 'upcoming', 'rocket']
    filter_horizontal = ['crew'] # 'images' removed needs adding back
    inlines = [PayloadInline]
