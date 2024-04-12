from .models import *
from rest_framework.serializers import ModelSerializer

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['images'] = ProductImageSerializer(instance.images.all(),many=True).data
        return repr

class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('title','image','price')
    
class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

