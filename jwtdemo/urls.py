# from django.urls import path
# from .views import registration

# urlpatterns = [
#     path('register/', registration, name='register')
# ]

from django.conf.urls import url
from django.conf.urls import include
from rest_framework import urlpatterns

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('user-viewset', views.UserViewset, basename='user-viewset')

urlpatterns =[
    url(r'',include(router.urls))
]