from django.contrib import admin

class ImageAdmin(admin.ModelAdmin):
    search_fields = ['image', 'type']
    #list_display = ['source', 'image', 'type', 'etag']
    list_filter = ['type']
