from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import BoardSerializer, PostSerializer, CommentSerializer


def home(request):
    return HttpResponse('Hello, World!')


class BoardView(APIView):
    def get(self, request, *args, **kwargs):
        board = Board.objects.all()
        serializer = BoardSerializer(board, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PostView(APIView):
    def get(self, request, *args, **kwargs):
        post = Posts.objects.filter(board=self.kwargs['pk'])
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CommentView(APIView):
    def get(self, request, *args, **kwargs):
        comment = Comments.objects.filter(post=self.kwargs['pid'])
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
