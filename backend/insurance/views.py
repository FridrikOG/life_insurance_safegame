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
import datetime


COVER_AMOUNT=2500000 
BASE_RATE=0.01
# Create your views here.
class InsuranceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    application = ApplicationSerializer()
    class Meta:
        model = Insurance
        optional_fields = ['dateCreated', 'dateApproved']
        fields = ('user','application', 'premium', 'application', 'dateCreated','dateApproved')
        
    def validate(self,data):
        if data['premium'] < 0:
            raise serializers.ValidationError("Premium must be 0 or greater")
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
    
    print("The files ", mortalityTable)
    return mortalityTable, riskLoads

def get_rate(age,gender,factors, mortalityTable, riskLoads):
    print("The age ", age )
    if gender=='male':
        #hazardRate=mortalityTable.loc[mortalityTable.Age == age,'Male_Hazard_Rate'].values[0]
        expectedLoss=mortalityTable.loc[mortalityTable.Age == age,'ExpectedLossMale'].values[0]
        # print("Expected loss ", expectedLoss)
        
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

    print('Your Annual Premium is:')

    return Annual_Premium



def checkHasPaid(insurance):
    print("Inside checkHasPaid ", insurance)

    ins = InsuranceSerializer(insurance)
 
    
    #print("seria ", ins.data)
    
@permission_classes([AllowAny])
class CreateAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer = None

    def post(self, request):
        ''' Get an insurance contract '''
        user = getUser(request)
        data = request.data
        mortalityTable, riskLoads  = getTables()
        application = Application.objects.filter(user=user.id, active=True).first()
        if not application:
            return JsonResponse({"message" : "No application found"}, status=status.HTTP_200_OK)
        insurance = Insurance.objects.filter(application=application)
        if not insurance:
            premium =get_rate(application.age,'male',['cancer'], mortalityTable, riskLoads)
            data = {'rate':premium}
            # User accepts the insurance contract
            print("Insurance baby ")
            print("The user ", user.id)
            print("Application  ", application.id)
            appJson = {
                "application" : application.id,
                "user" : user.id,
                "premium" : premium
            }
            ins = InsuranceSerializer(data=appJson)
            ins.is_valid(raise_exception=True)
            ins.save()
            insJson = InsuranceSerializer(ins)
            return JsonResponse({"data" : insJson.data}, status=status.HTTP_200_OK)
        insurance = insurance.first()
        insurance = InsuranceSerializer(insurance)
        return JsonResponse({"data" : insurance.data}, status=status.HTTP_400_BAD_REQUEST)
    
    

    def get(self, request):
        user = getUser(request)
        data = request.data
        mortalityTable, riskLoads  = getTables()
        application = Application.objects.filter(user=user.id, active=True).first()
        if not application:
            return JsonResponse({"message" : "No application found"}, status=status.HTTP_200_OK)
        insurance = Insurance.objects.filter(application=application)
        if not insurance:
            return JsonResponse({"data" : {}}, status=status.HTTP_200_OK)
        insurance = insurance.first()
        insurance = InsuranceSerializer(insurance)
        
        hasPaid = checkHasPaid(insurance)
        
        return JsonResponse({"data" : insurance.data}, status=status.HTTP_200_OK)
        
        
    def withdrawApplicatioN(self, request):
        
        return JsonResponse({"rate" : "Here"}, status=status.HTTP_200_OK)
    