from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True, required = True, style = {"input_type": "password"})
    password2 = serializers.CharField(
        style={"input": "password"}, write_only = True, label= "Confirm password")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
        ]

        # additional keyword arguments on fields, using the extra_kwargs option.
        # As in the case of read_only_fields, this means
        # you do not need to explicitly declare the field on the serializer.
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        # PUT THEIR DATA INTO DICTIONARY FOR BEING SERIALIZED
        ## validated_data is the dictionary that is being passed from the frontend 
        ## in case of angular validated data is the observable DI service that is being passed as a dictionary using forms through a browser
        ## via URL
        
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

        # CREATE THE USER BY PUTTING THE SERIALIZER DATA INTO THE USER OBJECT
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        return user

# class UserProfileSerializer(serializers.ModelSerializer):
#     #when ever you have a foreign key relation with a key that has its own serializer, use serializers.Prim... 
#     user = serializers.PrimaryKeyRelatedField(
#                 queryset=get_user_model().objects.all())

#     class Meta:
#         model = UserProfile
#         fields = ('__all__')

# from django.db import models
# from django.db.models import Sum
# from django.db.models.functions import Coalesce


# class AuthorManager(models.Manager):
#     def get_queryset(self):
#         return AuthorQuerySet(self.model, using=self._db)

#     def annotate_with_copies_sold(self):
#         return self.get_queryset().annotate_with_copies_sold()


# class AuthorQuerySet(models.QuerySet):
#     def annotate_with_copies_sold(self):
#         return self.annotate(copies_sold=Sum('books__copies_sold'))


# class Author(models.Model):
#     objects = AuthorManager()
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)


# class Book(models.Model):
#     title = models.CharField(max_length=30)
#     copies_sold = models.PositiveIntegerField()
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')