from django.contrib import admin
from . import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class EventResource(resources.ModelResource):
    class Meta:
        model = models.Event


@admin.register(models.Event)
class EventAdmin(ImportExportModelAdmin):
    resource_class = EventResource


@admin.register(models.EventParticipant)
class EventParticipantAdmin(admin.ModelAdmin):
    pass
