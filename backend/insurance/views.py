from django.shortcuts import render
from logging import raiseExceptions
from re import T
from application.serializers import ApplicationSerializer
from user.serializers import UserSerializer
from .models import User, Insurance, Application
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
from .serializers import InsuranceSerializer
from django.utils.timezone import make_aware

COVER_AMOUNT=2500000 
BASE_RATE=0.01
# Create your views here.
def getTables():
    print("PWD ", os.getcwd())
    mortalityTable=pd.read_csv('backend/insurance/MortalityTable.csv',sep=';')
    mortalityTable.head()
    riskLoads=pd.read_csv('backend/insurance/RiskLoads.csv',sep=';')
    riskLoads.head()
    riskLoads
    mortalityTable['ExpectedLossMale']=mortalityTable['Male_Hazard_Rate']*COVER_AMOUNT
    mortalityTable['ExpectedLossFemale']=mortalityTable['Female_Hazard_Rate']*COVER_AMOUNT
    mortalityTable.head()
    return mortalityTable, riskLoads

def getRate(age,gender = 'male',factors = []):
    mortalityTable, riskLoads = getTables()
    if gender=='male':
        #hazardRate=mortalityTable.loc[mortalityTable.Age == age,'Male_Hazard_Rate'].values[0]
        expectedLoss=mortalityTable.loc[mortalityTable.Age == age,'ExpectedLossMale'].values[0]
    else:
        #hazardRate=mortalityTable.loc[mortalityTable.Age == age,'Female_Hazard_Rate'].values[0]
        expectedLoss=mortalityTable.loc[mortalityTable.Age == age,'ExpectedLossFemale'].values[0]
    for x in factors:
        try:
            RiskLoad=riskLoads.loc[riskLoads.Factor== x,'RiskLoad'].values[0]
            RiskLoad_adjusted=RiskLoad*expectedLoss
            expectedLoss+=RiskLoad_adjusted
        except:
            print("Error ")
    # Yearly Premium as a percentage of cover amount
    TotalRate=BASE_RATE+(expectedLoss/COVER_AMOUNT)
    # Yearly premium (Expected loss+variable risk)
    Annual_Premium=(BASE_RATE*COVER_AMOUNT)+expectedLoss
    return int(Annual_Premium)

def getInsurance(application):
    return Insurance.objects.filter(application=application).first()

def acceptedInsurance(insurance):
    hasBeenPaid = checkHasPaid(insurance)
    insurance = InsuranceSerializer(insurance)
    insData = insurance.data
    if hasBeenPaid:
        insData['hasPaid'] = True
    else:
        insData['hasPaid'] = False
    return insData
    
@permission_classes([AllowAny])
class CreateAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer = None
    def post(self, request):
        ''' Get an insurance contract '''
        user = getUser(request)
        if not user:
            return JsonResponse({"message" : "User not authenticated"},status=status.HTTP_401_UNAUTHORIZED)
        userJson = UserSerializer( user ).data
        data = request.data
        application = getApplication(user.id)
        if not application:
            return JsonResponse({"message" : "Has insurance", "state":{"hasApplication":False, "hasInsurance":False}}, status=status.HTTP_400_BAD_REQUEST)
        insurance = getInsurance(application)
        applicationJson = ApplicationSerializer( application).data
        if not insurance:
            premium =getRate (application.age,'male',['cancer'])
            premium = int(premium)
            data = {'rate':premium}
            # User accepts the insurance contract
            appJson = {
                "application" : application.id,
                "user" :  user.id,
                "premium" : premium
            }
            Insurance(user=user, application=application, premium=premium).save()
            retDict = appJson
            retDict['state'] = {'hasInsurance' : True, 'hasApplication' : True}
            return JsonResponse(retDict, status=status.HTTP_200_OK)
        data = acceptedInsurance(insurance)
        data['application'] = applicationJson
        data['user'] = userJson
        data['state'] = {"hasApplication":True}
        return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = getUser(request)
        application = getApplication(user.id)
        if not user:
            return JsonResponse({"message" : "User not authenticated"},status=status.HTTP_401_UNAUTHORIZED)
        
        if not application:
            return JsonResponse({"message" : "Does not have an application", "state":{"hasApplication":False, "hasInsurance":False}}, status=status.HTTP_200_OK)
        # Get the insurance attached to the application if it exists
        insurance = getInsurance(application)
        print("Insurance ", insurance)
        if not insurance:
            premium = getRate(application.age)
            retDict = {}
            retDict['premium'] = premium
            retDict['state'] = {'hasInsurance' : False, 'hasApplication' : True}
            return JsonResponse(retDict, status=status.HTTP_200_OK)
        insData = acceptedInsurance(insurance)
        insData['hasApplication'] = True
        insData['hasInsurance'] = True
        return JsonResponse(insData, status=status.HTTP_200_OK)
    
    def withdrawApplication(self, request):
        return JsonResponse({"rate" : "Here"}, status=status.HTTP_200_OK)
    