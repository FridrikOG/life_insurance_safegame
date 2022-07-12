from django.shortcuts import render
from logging import raiseExceptions
from re import T
from application.serializers import ApplicationSerializer
from user.serializers import UserSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import status, generics, serializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
import pandas as pd
import numpy as np
import sys, os
from user.views import *
from application.views import *
from payment.function import checkHasPaid
import datetime
from django.utils.timezone import make_aware
from payment.function import *
from user.states import *
from .models import Package
from django.db.models import Sum
from math import floor

INSURANCE_IN_PACKAGE = 2
OUR_CUT  = 0.1

def createPackage():
    # This function really does not need to be very efficient
    # But needs to be clear and for the variables 
    insurances = Insurance.objects.filter(isPackaged=False)
    print("Count ", INSURANCE_IN_PACKAGE)
    print("Count insurance ", insurances.count())
    totalPrice = 0
    # If there are at least the amount of Insurance in a package
    if insurances.count() >= INSURANCE_IN_PACKAGE:
        insLis = insurances[0:INSURANCE_IN_PACKAGE]
        # Djang model sum
        sum = insLis.aggregate(Sum('premium'))
        # Now let's add the premium
       
        sum = sum['premium__sum'] * (1.0+OUR_CUT)
        sum = floor(sum)
        package = Package(soldFor=sum)
        package.save()
        
        for ins in insLis:
            package.insurances.add(ins)
            ins.isPackaged = True
            ins.save()
        return True
    return False
  
@permission_classes([AllowAny])
class PackageView(generics.GenericAPIView):
    def __init__(self):
        self.serializer = None
    def get(self, request):
        ''' Get all package insurances '''
        
        # package = Package(soldFor=500)
        # ins = Insurance.objects.get(id=2)
        # # Save the package so we can add the associated packages
        # package.save()
        # package.insurances.add(ins)
        ret = True
        while ret:
            ret = createPackage()
            
        
        
        return JsonResponse({}, status=status.HTTP_200_OK)

    def post(self, request):
        ''' Create a new package  '''
        
        
        
        
        
        return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)
