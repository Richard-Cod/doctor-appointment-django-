from django.apps import AppConfig
from backend.constants import getAppName


class DoctorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = getAppName('doctors')
