from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from consultation.models import ConsultantProfile, CustomerProfile


class ConsultantSerializer(serializers.ModelSerializer):
    '''
    Consultant model serializer
    '''

    class Meta:
        model = ConsultantProfile
        read_only_fields = ['name', ]
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    '''
        Customer model serializer
    '''

    class Meta:
        model = ConsultantProfile
        read_only_fields = ['name', ]
        fields = '__all__'


class SignupSerializer(serializers.ModelSerializer):
    '''
    a serializer for signup
    '''

    class Meta:
        model = CustomerProfile
        fields = ['user', 'date_of_birth']


class LoginSerializer(serializers.ModelSerializer):
    '''
    a serializer for login
    '''

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = CustomerProfile()
        fields = ['phone_number', 'password', 'email', ]
