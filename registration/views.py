from rest_framework import viewsets
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response


from . import models, serializers
from rest_framework.decorators import action


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

    def get_serializer_class(self):
        if self.action == "join":
            return serializers.EventParticipantSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=["post"])
    def join(self, request, pk=None):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(status=201)
