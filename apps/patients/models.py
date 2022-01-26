from django.db import models

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(
        "core.User",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"P - {self.user.email} - {self.user.id}"
    
