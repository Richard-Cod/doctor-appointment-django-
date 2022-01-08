from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Doctor, DoctorAward, DoctorEducation, DoctorFeature, DoctorService, DoctorSpecializations, DoctorWorkExperience
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email' ,'gender','first_name','last_name' , "profile_pic"]


class DoctorFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorFeature
        exclude = ("doctor",)

class DoctorEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorEducation
        exclude = ("doctor",)


class DoctorAwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAward
        exclude = ("doctor",)

class DoctorExperiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorWorkExperience
        exclude = ("doctor",)

class DoctorServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorService
        exclude = ("doctor",)

class DoctorSpecializationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSpecializations
        exclude = ("doctor",)               
        

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    features = DoctorFeatureSerializer(many=True)
    educations = DoctorEducationSerializer(many=True)
    awards = DoctorAwardsSerializer(many=True)
    experiences = DoctorExperiencesSerializer(many=True)
    services = DoctorServicesSerializer(many=True)
    specializations = DoctorSpecializationsSerializer(many=True)

    class Meta:
        model = Doctor
        fields = [ 
            'user', 'description' ,'speciality' ,'amount_per_our' ,
            'min_amount' ,'max_amount' ,'place' ,'about' , 'features' , 
            "educations" ,"awards","experiences","services","specializations" ]


