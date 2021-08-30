from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import DateFilter
from django_filters.rest_framework import FilterSet

from .models import Event
from .serializers import EventSerializer

from backend.tasks import send_email_save_event_error, save_event


class EventFilter(FilterSet):
    date_from = DateFilter(field_name='timestamp', lookup_expr='date__gte')
    date_to = DateFilter(field_name='timestamp', lookup_expr='date__lte')

    class Meta:
        model = Event
        fields = ('timestamp', 'category', 'session__id')


class EventViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions for Events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            save_event.delay(request.data)
        except ValidationError as error:
            http_origin = request.META.get('HTTP_ORIGIN')
            message = f'From {http_origin} \n'
            for key, value in error.detail.items():
                message += f'{key}: {value[0]} \n'
            send_email_save_event_error.delay(message)
        return Response({}, status=status.HTTP_200_OK)
