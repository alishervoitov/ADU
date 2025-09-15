from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.blog.models.contact import Contact
from .serializers import ContactSerializer


class ContactCreateView(generics.CreateAPIView):
    """
    Contact yaratish uchun API endpoint
    POST metodi bilan ishlaydi va permission talab qilmaydi
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'message': 'Xabaringiz muvaffaqiyatli yuborildi!',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )