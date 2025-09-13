from apps.blog.models.contact import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'full_name',
            'phone', 
            'message',
        )