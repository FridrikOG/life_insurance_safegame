from django.db import models
from user.models import User
# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator

import calendar
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta



def getYearFromNow():
    expiryOfInsurance = datetime.now(timezone.utc)
    expiryOfInsurance = datetime.strptime(str(expiryOfInsurance), "%Y-%m-%d")
    return expiryOfInsurance

# Create your models here.
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateTimeField()
    approved = models.BooleanField(default=True)
    dateApproved = models.DateTimeField(max_length=255, auto_now=True)
    active = models.BooleanField(default=True)
    dateCreated = models.DateTimeField(max_length=255, auto_now=True)

