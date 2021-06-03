from django.db import models
from django.db.models import fields
from django.db.models.fields import files
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Books, BorrowBook

# serializer for user model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
        return user
    
# serializer for Books model
class AllBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
    