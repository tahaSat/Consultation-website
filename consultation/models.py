from datetime import datetime, timedelta

from django.db import models
from core.models import BaseModel, User


class ConsultantProfile(BaseModel):
    '''
    a model for consultants that is also a user but has some extra fields
    '''
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=False, null=False)
    bio = models.TextField(max_length=1000, help_text='biograpgy of the consultant')
    expertise = models.CharField(max_length=255, help_text='expertise of the consultant')
    available_visit_time = models.JSONField(default=dict)


class CustomerProfile(BaseModel):
    '''
        a model for customer that is also a user but has some extra fields
    '''
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sign_up_date = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    consultants = models.ForeignKey(ConsultantProfile, on_delete=models.RESTRICT, blank=True, null=True)

    def age_range(self):
        age = datetime.now() - self.date_of_birth
        if age < timedelta(days=12*365):
            return 'child'
        elif age < timedelta(days=18*365):
            return 'teenager'
        elif age < timedelta(days=24*365):
            return 'young adult'
        elif age > timedelta(days=24*365):
            return 'adult'


class Consultation(BaseModel):
    '''
    a model for consultation
    '''
    user = models.OneToOneField(CustomerProfile, on_delete=models.CASCADE)
    consultant = models.ForeignKey(ConsultantProfile, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(default=datetime.now)
    duration = models.DurationField()
    status_choices = [('booked', 'Booked'), ('completed', 'Completed'), ('canceled', 'Canceled')]
    status = models.CharField(max_length=10, choices=status_choices, default='booked')
