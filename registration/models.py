from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=510)
    description = models.TextField()
    participants_allowed = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class EventParticipant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture = models.FileField(null=True)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
