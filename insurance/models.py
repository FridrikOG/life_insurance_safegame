from django.db import models
from user.models import User
from application.models import Application
from django.core.validators import MaxValueValidator, MinValueValidator
import time
import calendar
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

def getYearFromNow():
    expiryOfInsurance = datetime.now(timezone.utc) + relativedelta(years=1)
    expiryOfInsurance = expiryOfInsurance.strftime("%Y-%m-%d")
    expiryOfInsurance = datetime.strptime(str(expiryOfInsurance), "%Y-%m-%d")
    return expiryOfInsurance

def getCurrentDate():
    gmt = time.gmtime()
    ts = calendar.timegm(gmt)
    return ts



# Create your models here.
class Insurance(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    premium = models.IntegerField()
    dateExpires = models.DateTimeField(max_length=255, default= getYearFromNow())
    dateCreated = models.DateTimeField(max_length=255, auto_now=True)
    dateApproved = models.DateTimeField(max_length=255, auto_now=True)
    dateModified = models.DateTimeField(max_length=255, auto_now_add=True)