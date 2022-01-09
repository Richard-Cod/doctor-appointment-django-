from django.contrib import admin
from django.urls import path , include

from .views import DoctorViewSet, ListReviews

# urlpatterns = [
#     path('doctors/', DoctorViewSet.as_view() ),
#     path('doctor_reviews/', ListReviews.as_view() ),
# ]
