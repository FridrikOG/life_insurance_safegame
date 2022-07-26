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

import sys, os
from user.views import *
from application.views import *
from payment.function import checkHasPaid
import datetime
from .serializers import InsuranceSerializer
from django.utils.timezone import make_aware
from payment.function import *
from user.states import *
from .insuranceLogic import * 

def getInsurance(application):
    return Insurance.objects.filter(application=application).first()

def acceptedInsurance(insurance):
    hasBeenPaid = checkHasPaid(insurance)
    insurance = InsuranceSerializer(insurance)
    insData = insurance.data
    return insData
    
@permission_classes([AllowAny])
class CreateAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer = None
    def post(self, request):
        ''' Get an insurance contract '''
        
        
        
        state = getStateMessages()
        user = getUser(request)
        if not user:
            return JsonResponse({"message" : "User not authenticated", "state":state },status=status.HTTP_401_UNAUTHORIZED)
        userJson = UserSerializer( user ).data
        data = request.data
        application = getApplication(user.id)
        if not application:
            return JsonResponse({"message" : "Has insurance", "state":state}, status=status.HTTP_400_BAD_REQUEST)
        insurance = getInsurance(application)
        applicationJson = ApplicationSerializer( application).data
        state['hasApplication'] = True
        # Time to get the age
        age = getAge(application.dob)
        if not insurance:
            premium =getRate (age,'male',['cancer'])
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
            state['hasInsurance'] = True
            retDict['state'] = state
            return JsonResponse(retDict, status=status.HTTP_200_OK)
        retDict = acceptedInsurance(insurance)
        retDict['application'] = applicationJson
        retDict['user'] = userJson
        retDict['coverAmount'] = COVER_AMOUNT
        hasPayment = checkHasPaid(insurance)
        if hasPayment:
            state['hasPayment'] = True
        retDict['coverAmount'] = getCoverAmount()
        retDict['state'] = state
        return JsonResponse(retDict, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = getUser(request)
        application = getApplication(user.id)
        retDict = {}
        state = getStateMessages()
        if not user:
            return JsonResponse({"message" : "User not authenticated", "state" : state},status=status.HTTP_401_UNAUTHORIZED)
        
        if not application:
            return JsonResponse({"message" : "Does not have an application", "state":state}, status=status.HTTP_200_OK)
        state['hasApplication'] = True
        insurance = getInsurance(application)
        age = getAge(application.dob)
        if not insurance:
            premium = getRate(age)
            retDict = {}
            retDict['premium'] = premium
            # retDict['state'] = {'hasInsurance' : False, 'hasApplication' : True}
            retDict['state'] = state
            return JsonResponse(retDict, status=status.HTTP_200_OK)
        state['hasInsurance'] = True

        insData = acceptedInsurance(insurance)
        retDict = insData
        
        retDict['coverAmount'] = getCoverAmount()
        if checkHasPaid(insurance):
            state['hasPayment'] = True
        retDict['state'] = state
        
        return JsonResponse(retDict, status=status.HTTP_200_OK)
    
    def withdrawApplication(self, request):
        return JsonResponse({"rate" : "Here"}, status=status.HTTP_200_OK)
    