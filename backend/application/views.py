from django.shortcuts import render
from django.shortcuts import render
from logging import raiseExceptions
from re import T
from insurance.models import Insurance
from .models import *
from django.http import HttpResponse, JsonResponse
from rest_framework import status, generics, serializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from user.views import *
from .serializers import ApplicationSerializer


def getApplication(userId):
    return Application.objects.filter(user=userId, active=True).first()

@permission_classes([AllowAny])
class ApplicationAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer = None
    def post(self, request):
        ''' Get an insurance contract '''
        userId = getUserId(request)
        # userId will be false if the user is not logged in
        if not userId:
            return JsonResponse({"message" : "User not authenticated"},status=status.HTTP_401_UNAUTHORIZED)
        data = request.data
        data['user'] = userId
        item = ApplicationSerializer(data=request.data)
        item.is_valid(raise_exception=True)
        # Check if user has an active application
        # Can only have one active application at a time
        if Application.objects.filter(user=userId, active=True).exists():
            return JsonResponse({"message" : "User has an active application"} ,status=status.HTTP_401_UNAUTHORIZED)
        if item.is_valid():
            item.save()
            data = item.data
            data['state'] = {'hasApplication': True}
            return JsonResponse(data)
        else:
            data['state'] = {'hasApplication': False}
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        ''' Get the current active application '''
        userId = getUserId(request)
        if not userId:
            return JsonResponse({"message" : "User not authenticated"},status=status.HTTP_401_UNAUTHORIZED)
       # checking for the parameters from the URL
        applications = Application.objects.filter(user_id=userId, active=True)
        print('Applications here  ', applications)
        # if there is something in items else raise error
        if applications:
            application = applications.first()
            data = ApplicationSerializer(application).data
            data['state'] = {'hasApplication': True}
            return JsonResponse(data, status=status.HTTP_200_OK)
        else:
            data = {}
            data['state'] = {'hasApplication': False}
            return JsonResponse(data, status=status.HTTP_200_OK)
        
    def patch(self, request, id):
        # If not id
        if not id:
            return JsonResponse({"message" : "Application Id not found"},status=status.HTTP_404_NOT_FOUND)
        userId = getUserId(request)
        if not userId:
            return JsonResponse({"message" : "User not authenticated"},status=status.HTTP_401_UNAUTHORIZED)
        applications = Application.objects.filter(user_id=userId, id=id)
        if not applications:
            return JsonResponse({"message":"Application not found", "state": {"hasApplication" : False}}, status=status.HTTP_200_OK)
        application = applications.first()
        if application.active == False:
            return JsonResponse({"message":"Application not found", "state": {"hasApplication" : False}}, status=status.HTTP_200_OK)
        ins = Insurance.objects.filter(application=application.id)
        if ins:
            return JsonResponse({"message":"Already belongs to an Insurance", "state": {"hasApplication" : True, "hasInsurance":True}}, status=status.HTTP_200_OK) 
        serializer = ApplicationSerializer(application, data=request.data, partial=True) # set partial=True to update a data partially
        serializer.is_valid(raiseExceptions=True)
        serializer.save()
        data = serializer.data
        data['state'] = {'hasApplication': True}
        return JsonResponse({data}, status=status.HTTP_200_OK) 
        
        
def extractApplicationId(request):
    try:
        return request.data['applicationId']
    except:
        return False

class WithdrawApplicationAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer = None
    def post(self, request):
        ''' Withdraws the current active application if possible'''
        # if not id:
        #     return JsonResponse({"message" : "Application Id not found"},status=status.HTTP_404_NOT_FOUND)
        userId = getUserId(request)
        if not userId:
            return JsonResponse({"message" : "User not authenticated"},status=status.HTTP_401_UNAUTHORIZED)
        applications = Application.objects.filter(user_id=userId, active=True)
        if not applications:
            return JsonResponse({"message":"Application not found", "state": {"hasApplication" : False}}, status=status.HTTP_404_NOT_FOUND)
        application = applications.first()
        if application.active == False:
            return JsonResponse({"message":"Application is not active"}, status=status.HTTP_400_BAD_REQUEST)
        ins = Insurance.objects.filter(application=application.id)
        if ins:
            return JsonResponse({"message":"Already belongs to an Insurance"}, status=status.HTTP_400_BAD_REQUEST) 
        application.active = False
        application.save()
        app = ApplicationSerializer(application)
        data = app.data
        data['state'] = {'hasApplication': True}
        return JsonResponse(data, status=status.HTTP_200_OK)
        

class AllApplicationAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer = None
    def get(self, request):
        user = getUserId(request)
        if not user:
            return JsonResponse({"message" : "User not authenticated"},status=status.HTTP_401_UNAUTHORIZED)
        allApp = Application.objects.filter(user_id=user)
        if not allApp:        
            return Response({'applications':[]},status=status.HTTP_200)
        allApp = ApplicationSerializer(allApp, many=True)
        return JsonResponse({'applications':allApp.data})