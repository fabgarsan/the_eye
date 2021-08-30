from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer

from backend.tasks import save_event


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        save_event.delay(request.data)
        return Response({}, status=status.HTTP_200_OK)
