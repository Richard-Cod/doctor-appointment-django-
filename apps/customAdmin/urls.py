from django.contrib import admin
from django.urls import path , include

from apps.customAdmin import views

urlpatterns = [
    path('', views.home , name="doccure_home"  ),
    path('appointments-list', views.appointmentList , name="doccure_appointment_list"  ),
    path('doccure_specialities', views.specialities , name="doccure_specialities"  ),
    path('doccure_doctor_list', views.doctorsList , name="doccure_doctor_list"  ),
    path('doccure_patient_list', views.patientsList , name="doccure_patient_list"  ),
    path('doccure_reviews', views.reviews , name="doccure_reviews"  ),
    path('doccure_transactions_list', views.transactionsList , name="doccure_transactions_list"  ),
    path('doccure_settings', views.settings , name="doccure_settings"  ),
    path('doccure_invoice_report', views.invoiceReport , name="doccure_invoice_report"  ),
    path('doccure_profile', views.profile , name="doccure_profile"  ),
    
]
