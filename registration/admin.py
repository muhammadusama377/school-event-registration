from django.contrib import admin
from . import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventParticipant)
class EventParticipantAdmin(admin.ModelAdmin):
    pass
