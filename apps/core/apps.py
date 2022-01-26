from django.apps import AppConfig

from backend.constants import getAppName

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = getAppName("core")
