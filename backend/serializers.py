from rest_framework import serializers
from .models import *


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('name',
                  'description')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('name',
                  'description',
                  'created_on',
                  'updated_on',
                  'board',
                  'user')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('message',
                  'created_on',
                  'user',
                  'post')

