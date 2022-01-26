from django.apps import AppConfig

from backend.constants import getAppName


class AppointmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = getAppName("appointments")
    
