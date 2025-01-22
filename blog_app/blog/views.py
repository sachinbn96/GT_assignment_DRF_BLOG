from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer, UserSerializer


# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        blog = serializer.save()
        blog.assigned_users.add(self.request.user)

    def perform_update(self, serializer):
        blog = serializer.save()
        # if 'assigned_users' in self.request.data:
        #     blog.assigned_users.set(self.request.data['assigned_users'])
