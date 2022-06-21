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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    premium = models.IntegerField(default=0)
    dateCreated = models.DateField(max_length=255, auto_now_add=True)
    dateApproved = models.DateField(max_length=255, default = None)
    