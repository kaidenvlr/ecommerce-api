from rest_framework import serializers

from store.models import Category, Subcategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'image', 'active']
