from django.urls import path

from tests.views import *

APP_LABEL = 'tests'
urlpatterns = [
    path('question-api/', QuestionAPIView.as_view(), name='questions'),
    path('dass-api/', DASSApiView.as_view(), name='dass'),
    path('mbti-api/', MBTIApiView.as_view(), name='mbti'),

]
