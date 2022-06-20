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

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
       
        optional_fields = ['dateCreated', 'approved', ]
        fields = ('user','age', 'dateCreated', 'approved', 'active')


@permission_classes([AllowAny])
class ApplicationAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer = None
    def post(self, request):
        ''' Get an insurance contract '''
        user = getUserId(request)
        data = request.data
        data['user'] = user
        item = ApplicationSerializer(data=request.data)
        print("The item ", item.is_valid())
        item.is_valid(raise_exception=True)
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
        print('Applications ', applications)
        # if there is something in items else raise error
        if applications:
            application = applications.first()
            print('application ', applications.first())
            data = ApplicationSerializer(application)
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
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
        print('all app ', allApp)
        allApp = ApplicationSerializer(allApp, many=True)
        return JsonResponse({'applications':allApp.data})