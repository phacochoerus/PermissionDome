from rest_framework import serializers
from django.shortcuts import HttpResponse
from User import models
from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework.response import Response
from rest_framework import status





class studentsSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ["username","password"]


    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(username=validated_data["username"],password=validated_data["password"])
        models.Students.objects.create(user=user)
        return user


