from rest_framework import serializers
from apps.media_manage.models import News, NewType


class NewTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewType
        fields = ('id', 'name', 'description')


class NewsSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name', allow_null=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'type', 'content', 'viewed_count', 'created_at_str', 'updated_at_str')


class NewsShortSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name', allow_null=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'type', 'viewed_count', 'created_at_str', 'updated_at_str')