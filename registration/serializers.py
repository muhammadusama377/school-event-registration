from rest_framework import serializers
from . import models
from rest_framework.serializers import ValidationError


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = "__all__"


class EventParticipantSerializer(serializers.ModelSerializer):
    def validate(self, data):
        already_joined = models.EventParticipant.objects.filter(
            event=data["event"], email_address=data["email_address"]
        ).exists()

        if already_joined:
            raise ValidationError({"message": "you have already joined the event"})

        return data

    class Meta:
        model = models.EventParticipant
        fields = "__all__"
