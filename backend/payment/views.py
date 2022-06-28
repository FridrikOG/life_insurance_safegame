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
from datetime import datetime as dt
from rest_framework import status, generics, serializers
from dateutil.relativedelta import relativedelta

  
@permission_classes([AllowAny])
class PaymentAPIVIEW(generics.GenericAPIView):
    def get(self, request):
        ''' Get payment '''
        user = getUser(request)
        application = getApplication(user.id)
        if not application:
            return JsonResponse({"message" : "No application found"}, status=status.HTTP_200_OK)
        # get the insurance belonging to the user
        insurance = getInsurance(application)
        if not insurance:
            return JsonResponse({"data" : {}}, status=status.HTTP_200_OK)
        ins = InsuranceSerializer(insurance)
        hasPaid = checkHasPaid(insurance)
        if hasPaid:
            return JsonResponse({'hasPaid':True, 'paymentDue': ins.data['premium']}, status=status.HTTP_200_OK)
        paymentDue = getRate(application.age)

        return JsonResponse({'hasPaid':False, 'paymentDue': paymentDue}, status=status.HTTP_200_OK)
        
    def post(self, request):
        ''' Make payment'''
        user = getUser(request)

        application = getApplication(user.id)
        if not application:
            return JsonResponse({"message" : "No application found"}, status=status.HTTP_200_OK)
        # get the insurance belonging to the user
        insurance = getInsurance(application)
        if not insurance:
            return JsonResponse({"data" : {}}, status=status.HTTP_200_OK)
        ins = InsuranceSerializer(insurance)
        hasPaid = checkHasPaid(insurance)
        if hasPaid:
            return JsonResponse({'hasPaid':True, 'paymentDue': ins.data['premium']}, status=status.HTTP_200_OK)
        
        paymentDue = getRate(application.age)
        dict = {
            'insurance': insurance.id,
            'payment': paymentDue
        }
        insData = ins.data
        print("Ins data ", insData)
        insData['premium'] = 28000
 
        print("Ins data ", insData)

        print(insurance.dateCreated, type(insurance.dateCreated))
        expiryOfInsurance = dt.now() + relativedelta(years=1)
        insData['dateExpires'] = expiryOfInsurance
    
        
        
        serializer = InsuranceSerializer(insurance, data=insData, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        
        
        # IF there is no payment made, lets figure out the payment due
        
        payment = PaymentSerializer(data=dict)
        payment.is_valid(raise_exception=True)
        # payment.save()
        
        
        return JsonResponse({'hasPaid':True, 'paymentDue': paymentDue}, status=status.HTTP_200_OK)
        
    