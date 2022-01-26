from django.apps import AppConfig

from backend.constants import getAppName


class CustomadminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = getAppName('customAdmin')
