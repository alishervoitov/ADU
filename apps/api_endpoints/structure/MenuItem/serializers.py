from rest_framework import serializers
from apps.structure.models import MenuItem, Document


class DocumentSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    
    class Meta:
        model = Document
        fields = ['id', 'name', 'link', 'slug']
    
    def get_link(self, obj):
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
            return obj.file.url
        return obj.url


class MenuItemDetailSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True, read_only=True)
    
    class Meta:
        model = MenuItem
        fields = [
            'id', 
            'title', 
            'content', 
            'slug', 
            'view_count',
            'documents'
        ]

