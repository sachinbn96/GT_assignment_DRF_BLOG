from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class BlogSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description',
                  'assigned_users', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
