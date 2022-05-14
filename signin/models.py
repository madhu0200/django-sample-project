import email
from webbrowser import get
from django.db import connections
from django.db import models

class register(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    email=models.EmailField()
    mobileno=models.IntegerField()
    password=models.CharField(max_length=20)


class signuser(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    email=models.EmailField()
    mobileno = models.IntegerField()
    password=models.CharField(max_length=20)
    class Meta:
        db_table = "usersignin_register"
        managed=False
