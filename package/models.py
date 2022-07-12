from django.db import models
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import time
import calendar
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from insurance.models import Insurance

# Create your models here.
# Create your models here.
class Package(models.Model):
    soldFor = models.IntegerField(default=0)
    dateCreated = models.DateTimeField(max_length=255, auto_now=True)
    dateApproved = models.DateTimeField(max_length=255, auto_now=True)
    dateModified = models.DateTimeField(max_length=255, auto_now_add=True)
    insurances = models.ManyToManyField(Insurance, blank=True)