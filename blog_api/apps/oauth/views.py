from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class LoginOutView(APIView):
    def delete(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)