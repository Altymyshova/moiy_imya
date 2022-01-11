from rest_framework import serializers
from .models import Category , Product, Tag , Review

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
