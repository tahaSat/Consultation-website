from datetime import datetime, date

from django.db import transaction
from django.views.generic import ListView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from consultation.models import *
from consultation.serializers import *



class ListConsultantApi(ListView):
    model = ConsultantProfile()
    serializer = ConsultantSerializer()


class ListCustomerApi(ListView):
    model = CustomerProfile()
    serializer = CustomerSerializer()


class CustomUserSignupAPI(APIView):
    serializer = SignupSerializer()

    def get(self):
        return Response(data=self.serializer.data(), status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data()
        age = CustomerProfile.age_range(data)
        try:
            with transaction.atomic():
                user = User.objects.get_or_create(username=data['username'], password=data['password'],
                                                  )
                CustomerProfile.objects.get_or_create(user=user, date_of_birth=data['date_of_birth'],
                                                      sign_up_date=datetime.now(),
                                                      age_range=CustomerProfile.age_range())
        except:
            pass
        return Response(status=status.HTTP_201_CREATED)


class LoginAPI(APIView):
    serializer = LoginSerializer()

    def get(self, request):
        return Response(data=self.serializer.data(), status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data()
        username = data['username']
        password = data['password']
        try:
            user = User.objects.get(username=username)
        except:
            return Response(data='username not found', status=status.HTTP_401_UNAUTHORIZED)
            #write log
        if user.check_password(password):

            return Response(data=Token.objects.get(user=user), status=status.HTTP_200_OK)
        else:
            return Response(data='password is incorrect', status=status.HTTP_401_UNAUTHORIZED)


class ConsultationReservationAPI(APIView):
    '''
    api for reservation of a consultation, it also changes the time table of the consultant
    '''
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        '''
        overriding the get method for filtering active consultants only
        '''
        consultants = ConsultantProfile.objects.filter(is_active=True)
        return Response(data=consultants, status=status.HTTP_200_OK)

    def post(self, request):
        '''
           override post model to create a new object in consultation model and change the time table of the consultant
        '''
        data = request.data()
        try:
            with transaction.atomic():
                #prefetch_related('test') search shavad
                reserved_consultant = ConsultantProfile.objects.select_related().get(username=data['account'])
                Consultation.objects.create(user=AbstractUser.objects.get(username=data['user']),
                                            consultant=reserved_consultant,
                                            date=data['date'],
                                            time=data['time'],
                                            status='booked'
                                            )
        except:
            pass
        reserved_consultant.avaiable_visit_time[data['date']] = (data['time'], 'booked')
        return Response(status=status.HTTP_201_CREATED)


class ConsultationChangeStatusAPI(APIView):
    def post(self, request):
        data = request.data()
        # prefetch_related('test') search shavad
        Consultation.objects.get(id=data['id']).update(status=data['status'])
        consultant = ConsultantProfile.objects.get(id=data['id'])
        consultant.available_visit_time[data['date']] = (data['time'], data['status'])
        consultant.update()
        return Response(status=status.HTTP_200_OK)
