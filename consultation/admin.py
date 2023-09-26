from django.contrib import admin

from core.admin import BaseAdmin
from .models import *


class ConsultantAdmin(BaseAdmin):
    pass


class CustomerAdmin(BaseAdmin):
    pass


class ConsultationAdmin(BaseAdmin):
    pass


admin.site.register(ConsultantProfile, ConsultantAdmin)
admin.site.register(CustomerProfile, CustomerAdmin)
admin.site.register(Consultation, ConsultationAdmin)