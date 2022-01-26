from django.apps import AppConfig

from backend.constants import getAppName


class PatientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = getAppName('patients') 
