# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class Token(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING)
    secret = models.CharField(max_length=100)
