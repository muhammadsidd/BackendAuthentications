from django.contrib.auth import get_user_model
from rest_framework import permissions
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

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data = request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)

    res = {
        "refresh": str(refresh),
        "access":str(refresh.access_token),
    }

    return response.Response(res, status.HTTP_201_CREATED)

#POSSIBLE UPDATES TO THIS VERSION IN THE FUTURE

# class ProductListViewset(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class= ProductSerializer
#     # format = None
#
# class category_list_viewset(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CatogorySerializer
#     # format = None

# REST framework provides a set of already mixed-in generic views that we can use to trim down our views even more.
#
# class CategoryList(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CatogorySerializer


# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CatogorySerializer

# The create/retrieve/update/delete operations are pretty similar for any model-backed API views.
# Those bits of common behaviour are implemented in REST framework's mixin classes.
#
#  We're building our view using GenericAPIView, and adding in ListModelMixin and CreateModelMixin.
#
# The base class provides the core functionality, and the mixin classes provide the .list() and .create() actions.
# We're then explicitly binding the get and post methods to the appropriate actions.
# class CategoryList(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    generics.GenericAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CatogorySerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# # we're using the GenericAPIView class to provide the core functionality,
# # and adding in mixins to provide the .retrieve(), .update() and .destroy() actions.
# class CategoryDetail(mixins.UpdateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.DestroyModelMixin,
#                      generics.GenericAPIView ): #GEt, Put,Post, Delete
#     queryset = Category.objects.all()
#     serializer_class = CatogorySerializer
#
#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwrags):
#         return self.update(request, *args, **kwrags)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# REST framework introduces a Request and Response object :
# Request object extends the regular HttpRequest, and provides more flexible request parsing.
# The core functionality of the Request object is the request.data attribute,
# which is similar to request.POST, but more useful for working with Web APIs.

# Response object is a type of TemplateResponse that takes unrendered content
# and uses content negotiation to determine the correct content type to return to the client.

# class CategoryList(APIView):
#     def get(self, request, format=None):
#         categories = Category.objects.all()
#         categories = CatogorySerializer(categories, many=True)
#         return Response(categories.data)
#
#     def post(self,request, format=None):
#         categories = request.data()
#         categories = CatogorySerializer(categories)
#         if categories.is_valid():
#             categories.save()
#             return Response(categories.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(categories.data, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CategoryDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, Format=None):
#         category = CatogorySerializer(self.get_object(pk))
#         return Response(category.data)
#
#     def put(self, request, pk, format=None):
#         category = CatogorySerializer(self.get_object(pk))
#         category = CatogorySerializer(category, request.data)
#         if category.is_valid():
#             category.save()
#             return Response(category.data, status=status.HTTP_200_OK)
#         else:
#             return Response(category.data, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request, pk, format=None):
#         self.get_object(pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def category_list(request, format=None): #Web request object
#     if request.method == 'GET':
#         categories = Category.objects.all() #queryset to JSON
#         categories = CatogorySerializer(categories, many=True) #modelForm
#         return Response(categories.data) #Respose
#     elif request.method == 'POST': #inseting new records
#         categories = request.data() #JSON
#         categories = CatogorySerializer(categories) #
#         if categories.is_valid():
#             categories.save()
#             return Response(categories.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(categories.data, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET','PUT','DELETE'])
# def category_detail(request,pk, format=None):
#     try:
#         category = Category.objects.get(id=pk)
#     except Category.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     else:
#         if request.method == 'GET':
#            return Response(CatogorySerializer(category).data, status=status.HTTP_302_FOUND)
#         elif request.method == 'PUT': #update old record
#             category = CatogorySerializer(category, request.data)#JSON to Queryset
#             if category.is_valid():
#                 category.save()
#                 return Response(category.data, status=status.HTTP_200_OK)
#             else:
#                 return Response(category.data, status= status.HTTP_400_BAD_REQUEST)
#         elif request.method == 'DELETE':
#             category.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#
