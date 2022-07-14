from django.shortcuts import render
from logging import raiseExceptions
from re import T
from application.serializers import ApplicationSerializer
from package.serializer import PackageSerializer
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
import json


INSURANCE_IN_PACKAGE = 2
OUR_CUT  = 0.1

def createPackage():
    # This function really does not need to be very efficient
    # But needs to be clear and for the variables 
    insurances = Insurance.objects.filter(isPackaged=False)
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
        # This is better than it looks, this barely takes any time, but always
        # gets called when a user gets available packages
        ret = True
        while ret:
            ret = createPackage()
        
        packages = Package.objects.all()
        packageSer = PackageSerializer(data=packages, many=True)
        packageSer.is_valid()
        data = packageSer.data
        packages = json.loads(json.dumps(data))
        dict = {}
        print("Data ", packages)
        return JsonResponse({"packages": packages}, status=status.HTTP_200_OK)

    def post(self, request):
        ''' Create a new package  '''
        
        
        
        
        
        return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)
