from logging import raiseExceptions
from re import T
from .models import User
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.authentication import get_authorization_header
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from .serializers import LoginSerializer, LogOutSerializer, RegisterSerializer, UpdateProfileSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
import jwt
from django.utils.encoding import smart_str, force_str, force_bytes,  smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import *
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from django.shortcuts import redirect
from django.http import HttpResponsePermanentRedirect
import os


class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


def getUserId(request):
    ''' Takes in the HTTP request and extracts the token out of it'''
    auth = get_authorization_header(request).split()
    try:
        decoded = jwt.decode(auth[1].decode("utf-8"),
                         settings.SECRET_KEY, algorithms=['HS256'])
    except:
        return False
    return decoded['user_id']

def getUser(request):
    ''' Takes in the HTTP request and extracts the token out of it'''
    userId = getUserId(request)
    if not userId:
        return False
    user = User.objects.get(id=userId)
    return user


class TestAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer_class = RegisterSerializer
        self.serializer = None

    def get(self, request):
        return Response("Hello", status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class RegisterAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer_class = RegisterSerializer
        self.serializer = None

    def post(self, request):
        ''' Creates a new user '''

        self.serializer = self.serializer_class(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        # Grab the newly created user
        user = User.objects.get(email=request.data['email'])
        return Response(self.serializer.validated_data, status=status.HTTP_201_CREATED)


@permission_classes([AllowAny])
class LoginAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer_class = LoginSerializer
        self.serializer = None

    def post(self, request):
        ''' Login to an account '''
        self.serializer = self.serializer_class(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        user = User.objects.get(id=self.serializer.validated_data['id'])
        if not user.active:
            return Response({"detail": "User has been deleted"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.serializer.validated_data, status=status.HTTP_200_OK)

    def get(self, request):
        self.serializer = self.serializer_class(data=request.data)
        self.serializer.is_valid()
        return Response(request.header)


class LogOutAPIVIEW(generics.GenericAPIView):
    def __init__(self):
        self.serializer_class = LogOutSerializer
        self.serializer = None

    def post(self, request):
        ''' Logout from a session'''
        try:
            refresh = request.data['refresh']
            RefreshToken(refresh).blacklist()   # blacklists the refresh token
            return Response('Successfully logged out', status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Token not valid", status=status.HTTP_400_BAD_REQUEST)


def checkPassword(password, password2):
    if len(password) < 6:
        raise serializers.ValidationError({'password': 'password too short'})
    elif password != password2:
        raise serializers.ValidationError(
            {'password': 'passwords not the same'})




class UpdateProfile(generics.GenericAPIView):
    def __init__(self):
        self.serializer_class = UpdateProfileSerializer
        self.serializer = None

    def patch(self, request):
        ''' Update the profile of an authenticated user'''
        userId = getUserId(request)
        data = request.data
        user = User.objects.get(id=userId)

        if data['password'] != '':
            checkPassword(data['password'], data['password2'])
            user.set_password(data['password'])
        if data['firstname'] != '':
            if len(data['firstname']) > 30:
                return Response({"firstname": "firstname cannot exceed 30 characters"},
                                status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
            user.firstname = data['firstname']
        if data['lastname'] != '':
            if len(data['lastname']) > 30:
                return Response({"lastname": "lastname cannot exceed 30 characters"},
                                status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
            user.lastname = data['lastname']
        if data['imgURL'] != '':
            if len(data['imgURL']) > 255:
                return Response({"imgURL": "imgURL cannot exceed 255 characters"},
                                status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
            user.imgURL = data['imgURL']
        user.save()
        return Response({"user": user.getJson()}, status=status.HTTP_200_OK, content_type='application/json')

    def delete(self, request):
        ''' Delete user '''
        userId = getUserId(request)
        try:
            user = User.objects.get(id=userId, active=True)
        except:
            return Response("User does not exist", status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        retObj = user.getJson()
        retObj['isActive'] = user.active
        try:
            refresh = request.data['refresh']
            RefreshToken(refresh).blacklist()
        except:
            print("Token expired")
        return Response(retObj, status=status.HTTP_200_OK)



@permission_classes([AllowAny])
class PasswordTokenCheckAPIVIEW(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
        except:
            return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            checkToken = PasswordResetTokenGenerator().check_token(user, token)
            if checkToken:
                return Response({
                    "canResetPassword": True,
                    "token": token,
                    "uidb64": uidb64}, status=status.HTTP_200_OK
                )
            else:
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            redirect_url = request.data.get('redirect_url', '')
            # absurl = 'http://'+current_site  uidb64 + '&token=' + token
            absurl = 'http://' + 'https://annum-web.vercel.app/' + 'reset/password/complete?uidb64=' + \
                uidb64 + '&token=' + token
            email_body = 'Hello, \n Use the  below to reset your password  \n' + \
                absurl + '\n have a nice day!'
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
            dict = {'success': 'We have sent you a link to reset your password'}
            return Response(dict, status=status.HTTP_200_OK)
        else:
            dict = {'error': 'Email not found in our system'}
            return Response(dict, status=status.HTTP_400_BAD_REQUEST)



@permission_classes([AllowAny])
class SetNewPasswordAPIView(generics.GenericAPIView):

    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)


@permission_classes([])
class AdministrationAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)
