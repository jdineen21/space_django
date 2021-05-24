from django.contrib import admin

from .models import Rocket

class RocketAdmin(admin.ModelAdmin):
    pass

admin.site.register(Rocket, RocketAdmin)