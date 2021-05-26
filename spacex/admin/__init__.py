
from django.contrib import admin

from .launch import LaunchAdmin
from .launchpad import LaunchpadAdmin
from .rocket import RocketAdmin

from spacex.models import Launch, Launchpad, Rocket

admin.site.register(Launch, LaunchAdmin)
admin.site.register(Launchpad, LaunchpadAdmin)
admin.site.register(Rocket, RocketAdmin)