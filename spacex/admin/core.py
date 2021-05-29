from django.contrib import admin

class CoreAdmin(admin.ModelAdmin):
    search_fields = [
        'core',
        'block',
    ]
    list_display = [
        'serial',
        'block',
        'status',
    ]
    list_filter = [
        'block',
        'status',
    ]
