
from django.contrib import admin

from .core import CoreAdmin
from .landpad import LandpadAdmin
from .launch import LaunchAdmin
from .launchpad import LaunchpadAdmin
from .rocket import RocketAdmin

from spacex.models import Core, Landpad, Launch, Launchpad, Rocket

admin.site.register(Core, CoreAdmin)
admin.site.register(Landpad, LandpadAdmin)
admin.site.register(Launch, LaunchAdmin)
admin.site.register(Launchpad, LaunchpadAdmin)
admin.site.register(Rocket, RocketAdmin)