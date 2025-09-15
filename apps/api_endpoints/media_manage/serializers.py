from rest_framework import serializers
from apps.media_manage.models import News, NewType, DocumentType, Documents


class NewTypeChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewType
        fields = ('id', 'name', 'slug', 'parent')

class NewTypeSerializer(serializers.ModelSerializer):
    children=serializers.SerializerMethodField()
    class Meta:
        model = NewType
        fields = ('id', 'name', 'slug', 'children')
    
    def get_children(self, obj):
        if obj.subtypes.exists():
            return NewTypeChildrenSerializer(obj.subtypes.all(), many=True).data
        return []
            

class NewsSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name', allow_null=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'slug', 'image', 'video_url', 'type', 'content', 'viewed_count', 'created_at_str', 'updated_at_str')


class NewsShortSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name', allow_null=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'slug', 'image', 'video_url', 'type', 'viewed_count', 'created_at_str', 'updated_at_str')


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ('id', 'name', 'slug')


class DocumentsSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name', allow_null=True)

    class Meta:
        model = Documents
        fields = ('id', 'title', 'slug', 'url', 'type', 'created_at_str', 'updated_at_str')