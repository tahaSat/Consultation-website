from django.db import transaction

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from consultation.models import CustomerProfile
from tests.serializers import *


class QuestionAPIView(APIView):
    serializer = QuestionSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        test_name = request.data.get('test_name')
        Response(data=Question.objects.get(test_tag=test_name))


class DASSApiView(APIView):
    serializer = DASSSerializer()
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        Response(data=self.serializer.data(), status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data()
        try:
            with transaction.atomic():
                score = DASS.test_resaults(data['answers'])
                customer = CustomerProfile.objects.get(username=data['username'])
                DASS.objects.create(customer=customer, score=score, answers=data['answers'])

        except:
            pass

        Response(data=score, status=status.HTTP_201_CREATED)


class MBTIApiView(APIView):
    serializer = MBTISerializer()
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        Response(data=self.serializer.data(), status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data()
        try:
            with transaction.atomic():
                score = MBTI.test_resaults(data['answers'])
                customer = CustomerProfile.objects.get(username=data['username'])
                MBTI.objects.create(customer=customer, score=score, answers=data['answers'])

        except:
            pass

        Response(data=score, status=status.HTTP_201_CREATED)
