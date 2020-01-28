from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django_unixdatetimefield import UnixDateTimeField

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    created_at = UnixDateTimeField()
    desc = models.TextField()
    posted_at = UnixDateTimeField()

    def __str__(self):
        return self.question

    class Meta:
        ordering = ('posted_at',)


class User(AbstractUser):
    questions = models.ManyToManyField(Question, through='api.UserQuestion')
    mobile = models.CharField(max_length=10,
                              validators=[
                                  RegexValidator(
                                      regex=r'^[789]\d{9}$',
                                      message='Invalid Mobile Number',
                                  ),
                              ])

    def __str__(self):
        return self.mobile

    class Meta:
        ordering = ('mobile',)


class UserQuestion(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    response = models.CharField(max_length=20)
    created_at = UnixDateTimeField()

    class Meta:
        db_table = 'api_user_question'


class UserBackend(object):
    def authenticate(self, username=None, password=None):
        print 'hello'
        user = User.objects.get(username=username)
        return user
    def get_user(self, user_id):
        return User.objects.get(id=user_id)