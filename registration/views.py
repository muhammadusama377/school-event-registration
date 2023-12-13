from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


from . import models, serializers
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser


class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    parser_classes = [MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"

    def get_serializer_class(self):
        if self.action == "join":
            return serializers.EventParticipantSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=["post"])
    def join(self, request, pk=None):
        request.data["event"] = pk
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(status=201)
