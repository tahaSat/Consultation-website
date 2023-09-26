from rest_framework import serializers

from tests.models import DASS, MBTI, Question, Test


class QuestionSerializer(serializers.ModelSerializer):
    ''' A CLASS that serializes objects from test models'''

    class Meta:
        model = Question
        fields = '__all__'


class DASSSerializer(serializers.ModelSerializer):

    class Meta:
        model = DASS
        fields = '__all__'

class MBTISerializer(serializers.ModelSerializer):

    class Meta:
        model = MBTI
        fields = '__all__'