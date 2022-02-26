from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from rest_framework import serializers
from .models import Message
from apps.core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email' , 'id']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    class Meta:
        model = Message
        fields = "__all__"           
          

# class MessageSerializer(serializers.HyperlinkedModelSerializer):
#     user = UserSerializer()
#     message = MessageSerializer(many=True)

#     class Meta:
#         model = Doctor
#         fields = "*"


