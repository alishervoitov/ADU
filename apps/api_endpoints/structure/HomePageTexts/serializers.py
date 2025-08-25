from rest_framework import serializers
from apps.structure.models import HomePageText


class HomePageTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageText
        fields = ('title', 'description', 'type', "url", "banner")
    banner = serializers.SerializerMethodField()

    def get_banner(self, obj):
        request = self.context.get('request')
        if obj.banner and hasattr(obj.banner, 'url'):
            if request:
                return request.build_absolute_uri(obj.banner.url)
            return obj.banner.url
        return None


class HomePageSerializer(serializers.Serializer):
    main_text = serializers.SerializerMethodField()
    global_text = serializers.SerializerMethodField()
    academic_text = serializers.SerializerMethodField()
    history_text = serializers.SerializerMethodField()

    def get_main_text(self, obj):
        return HomePageTextSerializer(
            HomePageText.objects.filter(type='main'),
            many=True,
            context=self.context
        ).data

    def get_global_text(self, obj):
        return HomePageTextSerializer(
            HomePageText.objects.filter(type='global'),
            many=True,
            context=self.context
        ).data

    def get_academic_text(self, obj):
        return HomePageTextSerializer(
            HomePageText.objects.filter(type='academic'),
            many=True,
            context=self.context
        ).data

    def get_history_text(self, obj):
        return HomePageTextSerializer(
            HomePageText.objects.filter(type='history'),
            many=True,
            context=self.context
        ).data