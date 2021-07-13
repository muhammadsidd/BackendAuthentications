# from django.urls import path
# 

# urlpatterns = [
#     path('register/', registration, name='register')
# ]

from django.conf.urls import url
from django.conf.urls import include
from rest_framework import urlpatterns
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import registration
router = DefaultRouter()
router.register('user-viewset', views.UserViewset, basename='user-viewset')

urlpatterns =[
    url(r'',include(router.urls)),
    path('register/', registration, name = 'register')
]