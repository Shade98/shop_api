from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser,AllowAny
from .serializers import *

class PermissionMixin:
    def get_permissions(self):
        if self.action in ('retrieve,list'):
            permissions = [AllowAny]
        else:
            permissions = [IsAdminUser]
        return [permission() for permission in permissions]
    
class ProductViewSet(PermissionMixin,ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return self.serializer_class
    


class CategoryViewSet(PermissionMixin,ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductImageView(CreateAPIView):
    
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminUser]