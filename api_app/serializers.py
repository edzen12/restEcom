from rest_framework import serializers
from .models import Category, Product, Book


class CategorySerializer(serializers.ModelSerializer):
    """Категория"""
    class Meta:
        model = Category
        fields = (
            'id',
            'title'
        )


class BookSerializer(serializers.ModelSerializer):
    """Book"""
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'category',
            'author',
            'pages',
            'price',
            'stock',
            'description',
            'imageUrl',
            'status',
            'date_created',
        )


class ProductSerializer(serializers.ModelSerializer):
    """Product"""
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'price',
            'quantity',
            'description',
            'imageUrl',
            'status',
            'date_created',
        )


