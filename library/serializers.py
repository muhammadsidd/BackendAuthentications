from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Author, Book
from jwtdemo.serializers import UserSerializer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Author

class BookSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only = True)
    
    class Meta:
        fields = '__all__'
        model = Book