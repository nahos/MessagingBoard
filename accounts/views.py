from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializer import RegistrationSerializer


class RegistrationView(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors

        return Response(data)
