from rest_framework import serializers
from apps.structure.models import UniversityBaseInfo


class UniversityBaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityBaseInfo
        fields = "__all__"
