from django.db import models

from apps.doctors.models import Doctor
from apps.patients.models import Patient
from backend.constants import MONEY_TYPE, showPrice

# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )

    amount = models.DecimalField(max_digits=6 , decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Aptm : {showPrice(self.amount)} by {self.patient.user.first_name} for Dr.{self.doctor.user.last_name}"
    

