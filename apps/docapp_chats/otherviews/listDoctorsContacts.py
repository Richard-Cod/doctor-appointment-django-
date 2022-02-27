from rest_framework import serializers

from apps.core.models import User
from apps.docapp_chats.models import Message
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from apps.doctors.models import Doctor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id",'email' ,'gender','first_name','last_name' , "profile_pic"]

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    class Meta:
        model = Message
        fields = "__all__"   
        

class ListDoctorsContacts(APIView):
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]
    # queryset = DoctorReview.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, format=None):
        result = []
        doctors = Doctor.objects.all()
        for doc in doctors:
            content = "No msg yet 😶"
            messages = Message.objects.filter(sender__in=[request.user,doc.user],receiver__in=[request.user,doc.user])
            message = messages.last()
            if(message):
                content = message.content

            result.append({"user" :UserSerializer(doc.user).data,"lastMessage" : {"content" : content}})

        return Response(result)

class ListPatientsContacts(APIView):
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer

    def get(self, request, format=None):
        result = []
        users = User.objects.filter(doctor=None)
        for user in users:
            content = "No msg yet 😶"
            messages = Message.objects.filter(sender__in=[request.user,user],receiver__in=[request.user,user])
            message = messages.last()
            if(message):
                content = message.content

            result.append({"user" :UserSerializer(user).data,"lastMessage" : {"content" : content}})

        return Response(result)