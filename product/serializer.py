from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Product


# ModelSerializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Simple serializers
class MessageSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
