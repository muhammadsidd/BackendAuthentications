from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
      
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]

        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise serializers.ValidationError(
                {"email": "Email address must be unique."}
            )
        if password != password2:
            raise serializers.ValidationError(
                {"password": "The two passwords differ. "}
            )
        user = User.objects.create_user(**validated_data)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        return User.objects.update(instance,validated_data)

class UserViewset(viewset.Viewset):
    pass
