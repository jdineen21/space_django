from django.contrib import admin

class ImageAdmin(admin.ModelAdmin):
    search_fields = ['name', 'type']
    list_display = ['name']
    list_filter = ['type']
