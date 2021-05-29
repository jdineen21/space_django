from django.contrib import admin

class LandpadAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    list_filter = []
