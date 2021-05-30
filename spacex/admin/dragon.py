from django.contrib import admin

class DragonAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    list_filter = []
