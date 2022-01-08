from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import permissions
from doctors.models import Doctor

from doctors.serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]


