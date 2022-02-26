from django.shortcuts import get_object_or_404, render

from rest_framework import serializers

from .models import Message

from rest_framework import permissions
from .serializers import MessageSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from apps.core.models import User

from django.db import transaction



class ListMessages(APIView):
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]
    # queryset = DoctorReview.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, format=None):
        reviews = Message.objects.all()
        return Response(MessageSerializer(reviews , many=True).data)

class CreateMessage(APIView):
    http_method_names = ['post']
    permission_classes = [permissions.IsAuthenticated]
    # queryset = DoctorReview.objects.all()
    serializer_class = MessageSerializer

    @transaction.atomic
    def post(self, request, format=None):
        content = request.data.get("content")
        if(not content):
            return Response({"error" : "Please specify message content"},status=400)

        receiverId = request.data.get("receiverId")
        if(not receiverId):
            return Response({"error" : "Please specify receiverId"},status=400)

        message = Message(content=content,sender=request.user,senderID=request.user.id)

        receiver = get_object_or_404(User , pk=receiverId)
        message.receiver = receiver
        message.receiverID = receiver.id

        message.save()

        return Response(MessageSerializer(message).data)