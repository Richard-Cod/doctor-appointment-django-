from django.db import models


# Create your models here.
class Doctor(models.Model):
    
    user = models.OneToOneField(
        "core.User",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    description = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    amount_per_our = models.DecimalField(max_digits=6 , decimal_places=2)
    min_amount = models.DecimalField(max_digits=6 , decimal_places=2)
    max_amount = models.DecimalField(max_digits=6 , decimal_places=2)
    place = models.CharField(max_length=255)
    about = models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.email} - {self.user.id}"
    

class DoctorFeature(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="features" , on_delete=models.CASCADE)
    description = models.CharField(max_length=255 , blank=True)
    image = models.ImageField(upload_to="uploads/avatars/")

    def __str__(self) -> str:
        return f"{self.description} - {self.id}"


class DoctorEducation(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="educations" , on_delete=models.CASCADE)

    major = models.CharField(max_length=255)

    place = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f" - {self.id}"


class DoctorWorkExperience(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="experiences" , on_delete=models.CASCADE)

    place = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f" - {self.id}"


class DoctorAward(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="awards" , on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255 , blank=True)
    date = models.DateField()

    def __str__(self) -> str:
        return f" - {self.id}"


class DoctorService(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="services" , on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f" - {self.id}"


class DoctorSpecialization(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="specializations" , on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f" - {self.id}"


class DoctorLocation(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="locations" , on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    place = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6 , decimal_places=2)


    def __str__(self) -> str:
        return f" - {self.id}"


class DoctorReview(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="reviews" , on_delete=models.CASCADE)
    reviewer = models.ForeignKey("core.User", related_name="doctor_reviews" , on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_recommanding = models.BooleanField()
    description = models.TextField()

    class Meta:
        unique_together = ['reviewer', 'doctor']

    def __str__(self) -> str:
        return f" - {self.id}"




DEFAULT_HOURS = "07:00 AM - 09:00 PM"
class OpenHour(models.Model):
    monday = models.CharField(max_length=255 , default=DEFAULT_HOURS , blank=True)
    tuesday = models.CharField(max_length=255 , default=DEFAULT_HOURS , blank=True)
    wednesday = models.CharField(max_length=255 , default=DEFAULT_HOURS , blank=True)
    thursday = models.CharField(max_length=255 , default=DEFAULT_HOURS , blank=True)
    friday = models.CharField(max_length=255 , default=DEFAULT_HOURS , blank=True)
    saturday = models.CharField(max_length=255 , default=DEFAULT_HOURS , blank=True)
    sunday = models.CharField(max_length=255 , blank=True)

    doctor = models.OneToOneField(
        Doctor,
        related_name="openHours",
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self) -> str:
        return f" - {self.doctor.user.email}"
