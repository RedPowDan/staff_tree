from django.contrib import admin

from . import models

admin.site.register(models.Subdivision)
admin.site.register(models.Level)
admin.site.register(models.PositionAtWork)
