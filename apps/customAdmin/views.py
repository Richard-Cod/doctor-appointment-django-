from django.shortcuts import render

# from django.contrib.auth.decorators import login_required

# @login_required()

from django.contrib.auth.decorators import user_passes_test
from apps.appointments.models import Appointment

from apps.doctors.models import Doctor
from apps.patients.models import Patient
from backend.constants import showPrice
from django.db.models import Avg , Sum

@user_passes_test(lambda u: u.is_superuser)
def home(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()
    revenues = Appointment.objects.all().aggregate(Sum('amount'))["amount__sum"]
    return render(request, 'cadmin/index.html' , {
    "doctors" : doctors ,
    "patients" : patients,
    "appointments" : appointments,
    "revenues" : showPrice(revenues)
    })


@user_passes_test(lambda u: u.is_superuser)
def appointmentList(request):
    appointments = Appointment.objects.all()
    return render(request, 'cadmin/appointment-list.html' , {"appointments" : appointments,})


@user_passes_test(lambda u: u.is_superuser)
def specialities(request):
    return render(request, 'cadmin/specialities.html')


@user_passes_test(lambda u: u.is_superuser)
def doctorsList(request):
    return render(request, 'cadmin/doctor-list.html')

@user_passes_test(lambda u: u.is_superuser)
def patientsList(request):
    return render(request, 'cadmin/patient-list.html')

@user_passes_test(lambda u: u.is_superuser)
def reviews(request):
    return render(request, 'cadmin/reviews.html')

@user_passes_test(lambda u: u.is_superuser)
def transactionsList(request):
    return render(request, 'cadmin/transactions-list.html')

@user_passes_test(lambda u: u.is_superuser)
def settings(request):
    return render(request, 'cadmin/settings.html')

@user_passes_test(lambda u: u.is_superuser)
def invoiceReport(request):
    return render(request, 'cadmin/invoice-report.html')

@user_passes_test(lambda u: u.is_superuser)
def profile(request):
    return render(request, 'cadmin/profile.html')

@user_passes_test(lambda u: u.is_superuser)
def login(request):
    return render(request, 'cadmin/login.html')

@user_passes_test(lambda u: u.is_superuser)
def register(request):
    return render(request, 'cadmin/register.html')

@user_passes_test(lambda u: u.is_superuser)
def forgotPassword(request):
    return render(request, 'cadmin/forgot-password.html')