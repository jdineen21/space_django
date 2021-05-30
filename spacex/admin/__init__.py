
from django.contrib import admin

from .core import CoreAdmin
from .crew import CrewAdmin
from .dragon import DragonAdmin
from .landpad import LandpadAdmin
from .launch import LaunchAdmin
from .launchpad import LaunchpadAdmin
from .payload import PayloadAdmin
from .rocket import RocketAdmin

from spacex.models import Core, Crew, Dragon, Landpad, Launch, Launchpad, Payload, Rocket

admin.site.register(Core, CoreAdmin)
admin.site.register(Crew, CrewAdmin)
admin.site.register(Dragon, DragonAdmin)
admin.site.register(Landpad, LandpadAdmin)
admin.site.register(Launch, LaunchAdmin)
admin.site.register(Launchpad, LaunchpadAdmin)
admin.site.register(Payload, PayloadAdmin)
admin.site.register(Rocket, RocketAdmin)