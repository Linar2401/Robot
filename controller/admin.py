from django.contrib import admin

# Register your models here.

from controller.models import *

admin.site.register(RobotStatus)
admin.site.register(Package)
admin.site.register(Position)
admin.site.register(Command)
