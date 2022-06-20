from django.db import models
from user.models import User
# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
import time
import calendar


def getCurrentDate():
    gmt = time.gmtime()
    ts = calendar.timegm(gmt)
    return ts

# Create your models here.
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    approved = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    dateCreated = models.CharField(max_length=255, default=getCurrentDate())
