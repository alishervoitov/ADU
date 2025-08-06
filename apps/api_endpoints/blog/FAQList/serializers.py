from apps.blog.models import FAQ
from rest_framework import serializers


class FAQListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = (
            'question',
            'answer',
        )