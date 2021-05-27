
from django.contrib import admin

from .launch import LaunchAdmin, SignificantLaunchAdmin
from .launchpad import LaunchpadAdmin
from .rocket import RocketAdmin

from spacex.models import Launch, Launchpad, Rocket, SignificantLaunch

admin.site.register(Launch, LaunchAdmin)
admin.site.register(SignificantLaunch, SignificantLaunchAdmin)
admin.site.register(Launchpad, LaunchpadAdmin)
admin.site.register(Rocket, RocketAdmin)