from django.utils import timezone
from django.db import models
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField()

    def __str__(self):
        return f'{self.question_text}'

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))


class Choice(models.Model):
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.choice_text}'
