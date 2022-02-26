from django.shortcuts import get_list_or_404, render

# Create your views here.

from rest_framework import serializers, viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.doctors.models import Doctor, DoctorReview

from apps.doctors.serializers import DoctorSerializer

from apps.core.models import User

class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['gender','first_name','last_name']

# class DoctorSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = Doctor
#         fields = ['user']


class DoctorReviewsSerializer(serializers.ModelSerializer):
    reviewer = UserSerializer()
    # doctor = DoctorSerializer()
    class Meta:
        model = DoctorReview
        fields = ("id", 
                "doctor",
                "reviewer",
                "is_recommanding",
                "description",
)   



class ListReviews(APIView):
    http_method_names = ['get']
    permission_classes = [permissions.AllowAny]
    # queryset = DoctorReview.objects.all()
    serializer_class = DoctorReviewsSerializer

    def get(self, request, format=None):
        reviews = DoctorReview.objects.all()
        return Response(DoctorReviewsSerializer(reviews , many=True).data)


class ListDoctorReviews(APIView):
    http_method_names = ['get']
    permission_classes = [permissions.AllowAny]
    serializer_class = DoctorReviewsSerializer

    def get(self, request,doctorId , format=None):
        reviews = get_list_or_404(DoctorReview ,doctor=doctorId )
        # reviews = DoctorReview.objects.get(doctor=doctorId)
        
        return Response(DoctorReviewsSerializer(reviews , many=True).data)