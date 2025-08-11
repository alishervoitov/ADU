from rest_framework import serializers
from apps.media_manage.models import News, NewType, DocumentType, Documents


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


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ('id', 'name')


class DocumentsSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name', allow_null=True)

    class Meta:
        model = Documents
        fields = ('id', 'title', 'slug', 'url', 'type', 'created_at_str', 'updated_at_str')