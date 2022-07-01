from django.shortcuts import render
from logging import raiseExceptions
from re import T
from application.serializers import ApplicationSerializer
from user.serializers import UserSerializer
from insurance.serializers import InsuranceSerializer
from .models import Payment, Insurance
from .serializers import PaymentSerializer
from django.http import HttpResponse, JsonResponse
import sys, os
from user.views import *
from insurance.views import *
from rest_framework import status, generics, serializers 

from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

  
def getStateMessages():
    state = {
            "hasApplication": False,
            "hasInsurance": False,
            "hasPayment" : False
        }
    return state
  

def getYearFromNow():
    expiryOfInsurance = datetime.now(timezone.utc) + relativedelta(years=1)
    expiryOfInsurance = expiryOfInsurance.strftime("%Y-%m-%d")
    expiryOfInsurance = datetime.strptime(str(expiryOfInsurance), "%Y-%m-%d")
    return expiryOfInsurance

 

@permission_classes([AllowAny])
class PaymentAPIVIEW(generics.GenericAPIView):
    def get(self, request):
        ''' Get payment '''
        retDict = {}
        user = getUser(request)
        if not user:
            return JsonResponse({"message" : "User not authenticated"},status=status.HTTP_401_UNAUTHORIZED)
        application = getApplication(user.id)
        state = getStateMessages()
        if not application:
            return JsonResponse({"message" : "No application found", "state" : state}, status=status.HTTP_200_OK)
        # get the insurance belonging to the user
        insurance = getInsurance(application)
        state['hasApplication'] = True
        if not insurance:
            
            return JsonResponse({"message": "No insurance found", "state" : state}, status=status.HTTP_200_OK)
        ins = InsuranceSerializer(insurance)
        hasPaid = checkHasPaid(insurance)
        state['hasInsurance'] = True
        if hasPaid:
            retDict['premium'] = ins.data['premium']
            state['hasPayment'] = True
            retDict['state'] = state
            return JsonResponse(retDict , status=status.HTTP_200_OK)
        age = getAge(application.dob)
        paymentDue = getRate(age)
        retDict['state'] = state
        retDict['premium'] = paymentDue
        return JsonResponse(retDict, status=status.HTTP_200_OK)
        
    def post(self, request):
        ''' Make payment'''
        user = getUser(request)
        if not user:
            return JsonResponse({"message" : "User not authenticated"},status=status.HTTP_401_UNAUTHORIZED)
        application = getApplication(user.id)
        state = getStateMessages()
        if not application:
            return JsonResponse({"message" : "No application found", "state" : state}, status=status.HTTP_400_BAD_REQUEST)
        # get the insurance belonging to the user
        insurance = getInsurance(application)
        state['hasApplication'] = True
        if not insurance:
            return JsonResponse({"message": "No insurance found", "state" : state}, status=status.HTTP_400_BAD_REQUEST)
        ins = InsuranceSerializer(insurance)
        hasPaid = checkHasPaid(insurance)
        retDict = {}
        state['hasInsurance'] = True
        retDict['premium'] = ins.data['premium']
        if hasPaid:
            state['hasPayment'] = True
            retDict['state'] = state
            return JsonResponse(retDict, status=status.HTTP_400_BAD_REQUEST)
        age = getAge(application.dob)
        paymentDue = getRate(age)
        dict = {
            'insurance': insurance.id,
            'payment': paymentDue
        }
        insData = ins.data
        expiryOfInsurance = getYearFromNow()
        insData['dateExpires'] = expiryOfInsurance
        serializer = InsuranceSerializer(insurance, data=insData, partial=True)
        
        insurance.dateExpires = expiryOfInsurance
        
        serializer.is_valid(raise_exception=True)
        
        
        serializer.save()
        # If there is no payment made, 
        # lets figure out the payment due
        payment = PaymentSerializer(data=dict)
        
        payment.is_valid(raise_exception=True)
        payment.save()
        state['hasPayment'] = True
        retDict['state'] = state
        return JsonResponse(retDict, status=status.HTTP_200_OK)
        
    def delete(self, request):
        ''' Make payment'''
        user = getUser(request)
        if not user:
            return JsonResponse({"message" : "No application found", "state" : state}, status=status.HTTP_400_BAD_REQUEST)
        application = getApplication(user.id)
        state = getStateMessages()
        if not application:
            return JsonResponse({"message" : "No application found", "state" : state}, status=status.HTTP_400_BAD_REQUEST)
        # get the insurance belonging to the user
        insurance = getInsurance(application)
        state['hasApplication'] = True
        if not insurance:
            return JsonResponse({"message": "No insurance found", "state" : state}, status=status.HTTP_400_BAD_REQUEST)
        ins = InsuranceSerializer(insurance)
        hasPaid = checkHasPaid(insurance)
        retDict = {}
        state['hasInsurance'] = True
        retDict['premium'] = ins.data['premium']
        if hasPaid:
          
            retDict['state'] = state
            hasPaid.delete()
            
            return JsonResponse(retDict, status=status.HTTP_200_OK)
    
        return JsonResponse({ "message":"Has no payment", "state":state}, status=status.HTTP_400_BAD_REQUEST)
        
    