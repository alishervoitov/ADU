from apps.blog.models import InteractiveService
from rest_framework import serializers


class InteractiveServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractiveService
        fields = (
            'name',
            'link',
            'icon',
            'icon_dark',
            'order'
        )