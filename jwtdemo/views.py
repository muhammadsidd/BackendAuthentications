from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets, 
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCreateSerializer
# from django.http import Http404
# from django.shortcuts import render
# from rest_framework import viewsets, status, mixins, generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from api.serializers import ProductSerializer, CatogorySerializer
# from shop.models import Product, Category


User = get_user_model()

# @decorators.api_view(["POST"])
# @decorators.permission_classes([permissions.AllowAny])
# def registration(request):
#     serializer = UserCreateSerializer(data = request.data)
#     if not serializer.is_valid():
#         return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#     user = serializer.save()
#     refresh = RefreshToken.for_user(user)

#     res = {
#         "refresh": str(refresh),
#         "access":str(refresh.access_token),
#     }

#     return response.Response(res, status.HTTP_201_CREATED)

class UserViewset(viewsets.Viewset):
    pass
