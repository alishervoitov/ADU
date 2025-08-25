from rest_framework import serializers
from apps.structure.models import Divisions, DivisionDocument
from apps.api_endpoints.structure.Faculty.serializers import EmployeeSerializer
from django.db.models import Q


class DivisionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisions
        fields = ['id', 'name', 'icon', 'slug']


class DivisionDocumentSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    class Meta:
        model = DivisionDocument
        fields = ['id', 'name', 'link', 'slug']
    
    def get_link(self, obj):
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
            return obj.file.url
        return obj.url


class DivisionDetailSerializer(serializers.ModelSerializer):
    decan = EmployeeSerializer(read_only=True)
    documents = DivisionDocumentSerializer(many=True, read_only=True)
    class Meta:
        model = Divisions
        fields = [
            'id',
            'name',
            'content',
            'banner',
            'icon',
            'slug',
            'view_count',
            'decan',
            'documents'
        ]
