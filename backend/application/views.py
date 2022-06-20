from django.shortcuts import render
from django.shortcuts import render
from logging import raiseExceptions
from re import T
from .models import Application, User
from django.http import HttpResponse, JsonResponse
from rest_framework import status, generics, serializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from user.views import *
from .serializers import ApplicationSerializer


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
        # get data 
        data = request.data
        data['user'] = userId
        item = ApplicationSerializer(data=request.data)
        item.is_valid(raise_exception=True)
        
        if Application.objects.filter(user=userId, active=True ).exists():
            return JsonResponse({"message" : "User has an active application"} ,status=status.HTTP_200_OK)
        
        if Application.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')
        if item.is_valid():
            item.save()
            return JsonResponse(item.data)
        else:
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
            data = ApplicationSerializer(application)
            return Response(data.data)
        else: 
            return Response({"message":"User has no active application"}, status=status.HTTP_200_OK)
    
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