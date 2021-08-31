from rest_framework import serializers
from .models import Event
from django.utils import timezone


class EventSerializer(serializers.HyperlinkedModelSerializer):
    session_id = serializers.CharField()

    class Meta:
        model = Event
        fields = ['id', 'session_id', 'category', 'name', 'data', 'timestamp']

    def validate_timestamp(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("Timestamp is greater than real time")
        return value
