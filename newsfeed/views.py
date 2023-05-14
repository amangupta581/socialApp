from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
#from .serializers import UserSerializer, RegisterSerializer

from datetime import datetime


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


comment = Comment(email="leila@example.com", content="foo bar")


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


    class newsfeed(generics.GenericAPIView):
    serializer_class = CommentSerializer


serializer = CommentSerializer(comment)
serializer.data


def create(self, validated_data):
    return Comment(**validated_data)
