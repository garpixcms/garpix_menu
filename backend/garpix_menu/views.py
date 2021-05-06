from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuItemViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser, ]
    filter_backends = (DjangoFilterBackend, )
    filter_fields = {
        'title': ['icontains', ],
    }
