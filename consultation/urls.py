from django.contrib import admin
from django.urls import path

from consultation.views import *

APP_LABEL = 'consultations'
urlpatterns = [
    path('consultant-api/', ListConsultantApi.as_view(), name='consultant'),
    path('customer-api/', ListCustomerApi.as_view(), name='customer'),
    path('customuser-signup-api/', CustomUserSignupAPI.as_view(), name='custom-user-signup'),
    path('login-api/', LoginAPI.as_view(), name='login'),
    path('consultation-reservation-api/', ConsultationReservationAPI.as_view(), name='consultation-reservation'),
    path('consultation-change-api/', ConsultationChangeStatusAPI.as_view(), name='consultation-change-status'),

]
