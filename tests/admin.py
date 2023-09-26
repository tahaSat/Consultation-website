from django.contrib import admin

from core.admin import BaseAdmin
from .models import *


class DASSAdmin(BaseAdmin):
    pass


class MBTIAdmin(BaseAdmin):
    pass


class QuestionAdmin(BaseAdmin):
    pass


admin.site.register(DASS, DASSAdmin)
admin.site.register(MBTI, MBTIAdmin)
admin.site.register(Question, QuestionAdmin)