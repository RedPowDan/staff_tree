from django.contrib import admin

from . import models


class EmployeeTable(admin.ModelAdmin):
    readonly_fields = ("user",)


admin.site.register(models.Employee, EmployeeTable)
