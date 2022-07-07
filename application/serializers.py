from .models import Application, User
from rest_framework import  serializers
# fr
from user.function import *


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        optional_fields = [ 'dateCreated', 'approved']
        fields = ('user', 'dateCreated', 'approved', 'active', 'dob')
        # error_messages = {"age": {"required": "Give yourself a username"}}
    def validate(self,data):
        print("App seria  ", data)
        age = getAge(data['dob'])
        # if not data['dob']:
        #     raise serializers.validation.ValidationError("Age must be above 18")
        
        if age < 18:
            raise serializers.ValidationError("Age must be above 1")
        return data