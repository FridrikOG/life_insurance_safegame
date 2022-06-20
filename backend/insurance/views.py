from django.shortcuts import render
from logging import raiseExceptions
from re import T
from .models import User, Insurance
from django.http import HttpResponse, JsonResponse
from rest_framework import status, generics, serializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
import pandas as pd
import numpy as np
import sys, os
from user.views import *

COVER_AMOUNT=2500000 
BASE_RATE=0.01
# Create your views here.
class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        optional_fields = ['dateCreated', 'approved', ]
        fields = ('user','age', 'dateCreated', 'approved', 'active')
    def validate(self,data):
        if data['age'] < 1:
            raise serializers.ValidationError("Age must be above 1")
        return data


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

def get_rate(age,gender,factors, mortalityTable, riskLoads):

    if gender=='male':
        #hazardRate=mortalityTable.loc[mortalityTable.Age == age,'Male_Hazard_Rate'].values[0]
        expectedLoss=mortalityTable.loc[mortalityTable.Age == age,'ExpectedLossMale'].values[0]
        
    else:
        #hazardRate=mortalityTable.loc[mortalityTable.Age == age,'Female_Hazard_Rate'].values[0]
        expectedLoss=mortalityTable.loc[mortalityTable.Age == age,'ExpectedLossFemale'].values[0]
    
    for i in factors:
        print(i)
        RiskLoad=riskLoads.loc[riskLoads.Factor== i,'RiskLoad'].values[0]
        RiskLoad_adjusted=RiskLoad*expectedLoss
        expectedLoss+=RiskLoad_adjusted

    
    # Yearly Premium as a percentage of cover amount
    TotalRate=BASE_RATE+(expectedLoss/COVER_AMOUNT)

    # Yearly premium (Expected loss+variable risk)
    Annual_Premium=(BASE_RATE*COVER_AMOUNT)+expectedLoss

    print('Your Annual Premium is:')

    return Annual_Premium



@permission_classes([AllowAny])
class CreateAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer = None

    def post(self, request):
        ''' Get an insurance contract '''
        user = getUser(request)
        print('your user ', user)
        mortalityTable, riskLoads  = getTables()
        john=get_rate(age=24,gender='male', factors=['Smoker','CarOwner'], mortalityTable= mortalityTable, riskLoads=riskLoads)
        print("John bro ", john)
        return JsonResponse({}, status=status.HTTP_200_OK)

    def get(self, request):
        ''' Get an insurance contract '''
        user = getUser(request)
        data = request.data
        print('data to addd ', data )
        print('your user ', user)
        mortalityTable, riskLoads  = getTables()
        rate =get_rate(24,'male',['Smoker','CarOwner'], mortalityTable, riskLoads)
        print("John bro ", rate)

        return JsonResponse({"rate" : rate}, status=status.HTTP_200_OK)