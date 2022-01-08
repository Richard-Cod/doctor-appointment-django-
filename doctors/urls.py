from django.contrib import admin
from django.urls import path , include

from .views import DoctorViewSet

urlpatterns = [
    path('doctors/', DoctorViewSet.as_view() ),
]
