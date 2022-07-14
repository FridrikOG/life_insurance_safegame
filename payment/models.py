from django.db import models
from insurance.models import Insurance
# Create your models here.
import datetime
def getTimeStamp(date):
    return datetime.timestamp(date)

class Payment(models.Model):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    payment = models.IntegerField( default=0)
    isPaid = models.BooleanField(default=False)
    datePaid = models.DateTimeField(auto_now_add=True)