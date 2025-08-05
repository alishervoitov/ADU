from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.blog.models import InteractiveService
from . import serializers


class InteractiveServiceListView(ListAPIView):
    permission_classes = [AllowAny]
    pagination_class = None 
    serializer_class = serializers.InteractiveServiceListSerializer
    queryset = InteractiveService.objects.filter(is_active=True).order_by('order')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
