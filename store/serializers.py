from rest_framework import serializers

from main.serializers import UserSerializer
from store.models import Category, Subcategory, Brand, Product, Review, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'active']


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Subcategory
        fields = ['id', 'category', 'title', 'image', 'active']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title', 'image', 'active']


class ReviewSerializer(serializers.ModelSerializer):
    buyer = UserSerializer()

    class Meta:
        model = Review
        fields = ['id', 'content', 'star', 'buyer']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    subcategory = SubcategorySerializer()
    review = ReviewSerializer()

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'discount', 'image', 'review']
