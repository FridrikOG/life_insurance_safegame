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
# Create your views here.


class ItemApplication(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('user','age', 'dateCreated')


@permission_classes([AllowAny])
class CreateApplicationAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer = None

    def post(self, request):
        ''' Get an insurance contract '''
        user = getUserId(request)
        data = request.data
        data['user'] = user
        data['dateCreated'] = 0
        item = ItemApplication(data=request.data)
        print("The item ", item.is_valid() )
        item.is_valid(raise_exception=True)
        # validating for already existing data
        if Application.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')

        if item.is_valid():
            item.save()
            return JsonResponse(item.data)
        else:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
        

    def get(self, request):
        ''' Get application contract '''
        user = getUser(request)



        return JsonResponse({"rate" : 0}, status=status.HTTP_200_OK)