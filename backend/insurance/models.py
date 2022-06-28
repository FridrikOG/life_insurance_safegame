from django.db import models
from user.models import User
from application.models import Application
from django.core.validators import MaxValueValidator, MinValueValidator
import time
import calendar

def getCurrentDate():
    gmt = time.gmtime()
    ts = calendar.timegm(gmt)
    return ts

# Create your models here.
class Insurance(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    premium = models.IntegerField(default=0)
    dateExpires = models.DateField(max_length=255, auto_now_add=True)
    dateCreated = models.DateField(max_length=255, auto_now_add=True)
    dateApproved = models.DateField(max_length=255, auto_now_add=True)
    