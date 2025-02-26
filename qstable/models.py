from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UserScore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    correct_answers = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


