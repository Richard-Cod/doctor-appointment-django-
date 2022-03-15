from rest_framework import serializers

from apps.core.models import User
from apps.docapp_chats.models import Message
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from apps.docapp_chats.utils import getMessagesOfConversation
from apps.doctors.models import Doctor

from django.db.models import Q


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



def getContacts(currentUser,isPatient=True):
    result = []

    users = User.objects.filter(doctor__isnull=isPatient)

    for user in users:
        content = "No msg yet 😶"
        messages = getMessagesOfConversation(currentUser,user)
        message = messages.last()
        if(message):
            content = message.content

        result.append({"user" :UserSerializer(user).data,"lastMessage" : {"content" : content}})

    return result

class BaseContacts(APIView):
    isPatient = True

    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]
    # queryset = DoctorReview.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, format=None):
        result = getContacts(request.user,self.isPatient)
        return Response(result)

class ListDoctorsContacts(BaseContacts):
    isPatient = False

class ListPatientsContacts(BaseContacts):
    pass