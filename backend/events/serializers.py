from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    session_id = serializers.CharField()

    class Meta:
        model = Event
        fields = ['id', 'session_id', 'category', 'name', 'data', 'timestamp']
