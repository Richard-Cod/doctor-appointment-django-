from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Doctor)
admin.site.register(DoctorFeature)



admin.site.register(DoctorEducation)
admin.site.register(DoctorWorkExperience)
admin.site.register(DoctorAward)
admin.site.register(DoctorService)
admin.site.register(DoctorSpecializations)