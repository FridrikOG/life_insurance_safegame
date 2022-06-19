from django.shortcuts import render
from django.shortcuts import render
from logging import raiseExceptions
from re import T
from .models import User
from django.http import HttpResponse, JsonResponse
from rest_framework import status, generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from user.views import *

# Create your views here.


@permission_classes([AllowAny])
class CreateApplicationAPIVIEW(generics.GenericAPIView):
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
        print('your user ', user)
        mortalityTable, riskLoads  = getTables()
        rate =get_rate(24,'male',['Smoker','CarOwner'], mortalityTable, riskLoads)
        print("John bro ", rate)
    
        return JsonResponse({"rate" : rate}, status=status.HTTP_200_OK)