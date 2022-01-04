from django.contrib import admin

class CrewAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
