from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories',CategoryViewSet)
router.register('products',ProductViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('add-product-image/',ProductImageView.as_view())
]