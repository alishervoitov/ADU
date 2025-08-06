from rest_framework import serializers
from apps.structure.models import HomePageText


class HomePageTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageText
        fields = ('title', 'description', 'type', "url")

class HomePageSerializer(serializers.Serializer):
    main_text = serializers.SerializerMethodField()
    global_text = serializers.SerializerMethodField()
    academic_text = serializers.SerializerMethodField()
    history_text = serializers.SerializerMethodField()

    def get_main_text(self, obj):
        return HomePageTextSerializer(HomePageText.objects.filter(type='main'), many=True).data

    def get_global_text(self, obj):
        return HomePageTextSerializer(HomePageText.objects.filter(type='global'), many=True).data

    def get_academic_text(self, obj):
        return HomePageTextSerializer(HomePageText.objects.filter(type='academic'), many=True).data

    def get_history_text(self, obj):
        return HomePageTextSerializer(HomePageText.objects.filter(type='history'), many=True).data