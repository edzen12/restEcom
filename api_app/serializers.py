from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Product, Book


class CategorySerializer(serializers.ModelSerializer):
    """Category"""
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    """Book"""
    class Meta:
        model = Book
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """Product"""
    class Meta:
        model = Product
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """User"""
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'books',
            'products'
        )