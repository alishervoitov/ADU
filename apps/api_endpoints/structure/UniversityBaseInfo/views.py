from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.structure.models import UniversityBaseInfo
from . import serializers


class UniversityBaseInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        texts = UniversityBaseInfo.objects.first()
        serializer = serializers.UniversityBaseInfoSerializer(texts)
        return Response(serializer.data)
