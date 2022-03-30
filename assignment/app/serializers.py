from rest_framework import serializers

from .models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer to get all categories """

    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at')


class SubCategorySerializer(serializers.ModelSerializer):
    """ Serializer to get subcategories for a category """

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'created_at')


class ProductSerializer(serializers.ModelSerializer):
    """ Serializer to get all products for a category """

    class Meta:
        model = Product
        fields = ('id', 'name', 'created_at')
