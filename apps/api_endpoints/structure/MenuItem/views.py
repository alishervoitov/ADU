from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from apps.structure.models import MenuItem
from apps.structure.enum import MenuItemEnum
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class MenuItemByTypeView(RetrieveAPIView):
    """
    Retrieve MenuItem by menu_type
    """
    permission_classes = [AllowAny]
    serializer_class = serializers.MenuItemDetailSerializer
    lookup_field = 'menu_type'
    
    def get_queryset(self):
        return MenuItem.objects.select_related().prefetch_related('documents')
    
    def get_object(self):
        menu_type = self.kwargs['menu_type']
        
        # Validate that menu_type is a valid enum value
        valid_menu_types = [item.value for item in MenuItemEnum]
        if menu_type not in valid_menu_types:
            return None
            
        obj = get_object_or_404(self.get_queryset(), menu_type=menu_type)
        
        # Increment view count
        obj.view_count += 1
        obj.save(update_fields=['view_count'])
        
        return obj
    
    @swagger_auto_schema(
        operation_description="Get MenuItem by menu type",
        manual_parameters=[
            openapi.Parameter(
                'menu_type',
                openapi.IN_PATH,
                description="Menu type (charter, history, council, scientific_council)",
                type=openapi.TYPE_STRING,
                enum=[item.value for item in MenuItemEnum]
            )
        ],
        responses={
            200: serializers.MenuItemDetailSerializer,
            404: "MenuItem not found"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
