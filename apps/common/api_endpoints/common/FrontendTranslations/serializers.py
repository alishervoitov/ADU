from apps.common import models
from rest_framework import serializers

from apps.common.utils.get_lang import get_language

class FrontendTranslationSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()
    
    class Meta:
        model = models.FrontendTranslation
        fields = ("key", "text")
    
    def get_text(self, obj):

        current_language = get_language(self.context.get("request"))

        print(f"Detected lang: {current_language}")

        if current_language == 'uz' or current_language is None:
            return obj.text

        if current_language == 'cyrl':
            return getattr(obj, 'text_uz_cyrl', obj.text) or obj.text
        elif current_language == 'ru':
            return getattr(obj, 'text_ru', obj.text) or obj.text
        elif current_language == 'en':
            return getattr(obj, 'text_en', obj.text) or obj.text

        return obj.text


class FrontendTranslationCreateSerializer(serializers.ModelSerializer):
    text_uz_cyrl = serializers.CharField(required=False, allow_blank=True)
    text_ru = serializers.CharField(required=False, allow_blank=True)
    text_en = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = models.FrontendTranslation
        fields = ("key", "text", "text_uz_cyrl", "text_ru", "text_en")
    
    def create(self, validated_data):
        return models.FrontendTranslation.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
