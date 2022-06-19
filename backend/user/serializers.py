from ast import Pass
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, min_length=6)
    password = serializers.CharField(max_length=255, min_length=6)
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials')

        return {
            "id": user.id,
            'email': user.email,
            'password': password,
            'password2': password,
            'username': user.username,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'imgURL': user.imgURL,
            'date': user.date,
            'tokens': user.tokens(),
        }


class LogOutSerializer(serializers.Serializer):
    pass


class RegisterSerializer(serializers.ModelSerializer):
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'firstname', 'lastname',
                  'username', 'imgURL', 'tokens']  # Fields that are returned from validate e.g
        extra_kwargs = {
            'password': {'error_messages': {'miss-match': "Passwords do not match"}},
        }

    def create_user(self, data):
        user = User.objects.create_user(data)
        tokens = user.tokens()
        return {"tokens": tokens, "user": user}

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        firstname = attrs.get('firstname', '')
        lastname = attrs.get('lastname', '')
        username = attrs.get('username', '')
        imgURL = attrs.get('imgURL', '')

        # Custom ValidationError exception for the password field
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords do not match'})

        data = self.create_user({"email": email, "password": password, "password2": password2,
                                 "firstname": firstname, "lastname": lastname, "username": username, "imgURL": imgURL})

        return {
            'id': data['user'].id,
            'email': data['user'].email,
            'password': data['user'].password,
            'password2': data['user'].password2,
            'firstname': data['user'].firstname,
            'lastname': data['user'].lastname,
            'username': data['user'].username,
            'imgURL': data['user'].imgURL,
            "tokens": data['tokens'],
        }


class UpdateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'firstname', 'lastname',
                  'username', 'imgURL']  # Fields that are returned from validate e.g

    def update_user(self):
        User.objects.update(self.validated_data)

    def validate(self, attrs):
        email = attrs.get('email', '')
        firstname = attrs.get('firstname', '')
        lastname = attrs.get('lastname', '')
        username = attrs.get('username', '')
        imgURL = attrs.get('imgURL', '')

        return {
            'email': email,
            'firstname': firstname,
            'lastname': lastname,
            'username': username,
            'imgURL': imgURL,
        }


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        field = ['email']

    def validate(self, attrs):

        email = attrs['data'].get('email', '')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(user.id)
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=attrs['data'].get('request')).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            absurl = 'http://'+current_site + relativeLink
            email_body = 'Hi ' + user.username + 'use link below to reset your password'
            data = {
                'email_body': email_body, 'to_meial': user.email, 'email_subject': 'Reset password'}

        return super().validate(attrs)


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)
