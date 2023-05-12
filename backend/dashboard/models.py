from django.contrib.auth.models import User
from django.db import models


class Filter(models.Model):
    name = models.CharField(max_length=250)
    active = models.CharField(max_length=1, choices=[('A', 'Active'), ('I', 'Inactive')], default='A')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now=True)


class Keyword(models.Model):
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    value = models.CharField(max_length=500)
    date_create = models.DateTimeField(auto_now=True)


class Alert(models.Model):
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    date_create = models.DateTimeField(auto_now=True)
