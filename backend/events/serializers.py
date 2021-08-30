from rest_framework import serializers
from .models import Event, Session, Application


class EventSerializer(serializers.HyperlinkedModelSerializer):
    session_id = serializers.CharField()

    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name', 'data', 'timestamp']
