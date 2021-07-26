from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from rest_framework.views import APIView
from basicpermissions.views import IsOwner
from re import search
from django.contrib.auth import authenticate, get_user_model
from django.db.models import query
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, serializers
from rest_framework import response, decorators, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, Token
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from . import models
from .import permissions1
from jwtdemo import serializers
from rest_framework import filters
import json
# from django.http import Http404
# from django.shortcuts import render
# from rest_framework import viewsets, status, mixins, generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from api.serializers import ProductSerializer, CatogorySerializer


User = get_user_model()

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserSerializer(data = request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)

    res = {
        "refresh": str(refresh),
        "access":str(refresh.access_token),
    }

    return response.Response(res, status.HTTP_201_CREATED)

class UserViewset(viewsets.ViewSet):
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions1.UpdateOwnProfile,)
    serializer_class = UserSerializer
    filter_backends =(filters.SearchFilter,)
    search_fields = ('email','first_name','last_name')

    def list(self, request):
        queryset = User.objects.all()
        serializer = self.serializer_class(queryset, many = True)
        
        return Response(serializer.data)
    
    def create(self, request):
        if request.user.is_authenticated:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(
                    created_by=request.user,
                    modified_by=request.user
                )
                return Response(serializer.data, status=201)
        
        raise PermissionDenied
    
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
    def update(self, request, pk = None):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class FibNumViewset(APIView):
    def get (self, reuest, format= None):
        nterms = int(input("How many terms? "))
        # first two terms
        n1, n2 = 0, 1
        count = 0
        l1=[]
        l2=[]

        # check if the number of terms is valid
        if nterms <= 0:
            print("Please enter a positive integer")
        elif nterms == 1:
            print("Fibonacci sequence upto", nterms, ":")
            print(n1)
        else:
            print("Fibonacci sequence")
            while count < nterms: 
                l1.append(count)
                l2.append(n1)
                print(n1)
                nth = n1 + n2
                # update values
                n1 = n2
                n2 = nth
            
                count += 1
        d1= dict(zip(l1,l2))
        return Response (json.dumps(d1)




