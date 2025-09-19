from apps.blog.models import InteractiveService
from rest_framework import serializers


class InteractiveServiceListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    link = serializers.URLField()
