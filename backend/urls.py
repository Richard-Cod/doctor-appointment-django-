"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

from rest_framework import routers
from apps.doctors import views


from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()
router.register(r'doctors', views.DoctorViewSet)
# router.register(r'doctor_reviews', views.ListReviews)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadmin/', include('apps.customAdmin.urls')),
    path('djoser/', include('djoser.urls')),
    path('authjwt/', include('djoser.urls.jwt')),

    path('api/doctor_reviews/', views.ListReviews.as_view()),
    path('api/doctor_reviews/<int:doctorId>', views.ListDoctorReviews.as_view()),

    path('api/', include(router.urls)),

     path('api-auth/', include('rest_framework.urls'))
]+ static(settings.STATIC_URL , document_root=settings.MEDIA_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)