from django.db import models
from insurance.models import Insurance
# Create your models here.


class Payment(models.Model):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    
    payment = models.IntegerField(max_length=100, default=0)
    datePaid = models.DateTimeField(auto_now_add=True)