from django.db import models

from consultation.models import CustomerProfile
from core.models import BaseModel


class Question(BaseModel):
    '''
    a model which contains the questions
    '''
    question_number = models.PositiveIntegerField(null=False, blank=False)
    question_body = models.TextField(blank=False, null=False)
    tag_choices = [('Dass', 'DASS'), ("Mbti", 'MBTI'), ]
    test_tag = models.CharField(max_length=50, choices=tag_choices)


class Test(BaseModel):
    class Meta:
        abstract = True

    '''
    each object contains a test for a customer specs
    '''
    customer = models.OneToOneField(CustomerProfile, on_delete=models.CASCADE)
    score = models.TextField()
    answers = models.JSONField(blank=False, null=False)


class DASS(Test):

    def test_resaults(self):
        deppression_score = sum(self.answers[0:6])
        anxiety_score = sum(self.answers[7:13])
        stress_score = sum(self.answers[14:20])
        return deppression_score, anxiety_score, stress_score


class MBTI(Test):

    def test_resaults(answers):
        e_list = [(1, 1), (1, 2), (1, 2), (2, 1), (2, 2), (1, 1), (1, 2), (2, 0), (2, 1), (1, 0), (1, 2), (2, 2),
                  (2, 1), (2, 2), (1, 0), (2, 2), (2, 2), (1, 2), (1, 2), (1, 2), (1, 1), (1, 2), (1, 1), (1, 1),
                  (1, 1)]
        i_list = [(2, 2), (2, 2), (2, 2), (1, 0), (1, 1), (2, 1), (2, 2), (1, 1), (1, 0), (2, 1), (2, 2), (1, 2),
                  (1, 2),
                  (1, 1), (2, 1), (1, 1), (1, 2), (2, 1), (2, 2), (2, 2), (2, 1), (2, 0), (2, 2), (2, 2), (2, 1)]
        s_list = [(1, 2), (2, 1), (1, 2), (2, 2), (1, 2), (2, 2), (1, 2), (1, 2), (1, 2), (1, 1), (1, 2), (1, 1),
                  (1, 1),
                  (1, 0), (1, 2), (1, 0), (2, 0), (2, 2), (2, 2)]
        n_list = [(2, 2), (1, 1), (2, 2), (1, 2), (2, 1), (1, 1), (2, 1), (2, 1), (2, 2), (2, 1), (2, 2), (2, 1),
                  (2, 1),
                  (2, 2), (2, 1), (2, 2), (1, 1), (1, 1), (1, 2)]
        t_list = [(1, 1), (2, 2), (2, 1), (2, 1), (2, 0), (2, 0), (1, 1), (1, 1), (2, 2), (1, 2), (2, 1), (1, 1),
                  (1, 2),
                  (1, 0), (1, 2), (2, 1), (1, 2), (2, 2), (1, 0), (2, 1), (1, 2), (2, 2), (2, 2), (2, 2)]
        f_list = [(2, 0), (1, 1), (1, 1), (1, 0), (1, 1), (1, 1), (2, 0), (2, 0), (1, 2), (2, 2), (1, 1), (2, 1),
                  (2, 2),
                  (2, 2), (2, 0), (1, 0), (2, 0), (1, 1), (2, 2), (1, 1), (1, 0), (1, 0)]
        j_list = [(1, 0), (1, 1), (1, 2), (1, 1), (1, 1), (1, 2), (2, 1), (1, 1), (1, 2), (2, 1), (1, 2), (1, 2),
                  (1, 1),
                  (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 1), (1, 1)]
        p_list = [(2, 2), (2, 1), (2, 2), (2, 2), (2, 2), (2, 2), (1, 2), (2, 2), (2, 2), (1, 1), (2, 1), (2, 2),
                  (2, 0),
                  (2, 1), (2, 2), (2, 2), (2, 2), (2, 1), (2, 2)]

        e = i = s = n = t = f = j = p = 0
        for i in range(24):
            if answers[i] == e_list[i][0]:
                e += e_list[i][1]
            else:
                i += i_list[i][1]

        for i in range(25, 43):
            if answers[i] == s_list[i][0]:
                s += s_list[i][1]
            else:
                n += n_list[i][1]

        for i in range(44, 67):
            if answers[i] == t_list[i][0]:
                t += t_list[i][1]
            else:
                f += f_list[i][1]

        for i in range(68, 86):
            if answers[i] == j_list[i][0]:
                j += j_list[i][1]
            else:
                p += p_list[i][1]
        if e > i:
            a1 = 'E'
        else:
            a1 = 'I'
        if s > n:
            a2 = 'S'
        else:
            a2 = 'N'
        if t > f:
            a3 = 'T'
        else:
            a3 = 'F'
        if j > p:
            a4 = 'J'
        else:
            a4 = 'p'

        return a1 + a2 + a3 + a4
