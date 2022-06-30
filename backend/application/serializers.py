from .models import Application, User
from rest_framework import  serializers

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        optional_fields = [ 'dateCreated', 'approved']
        fields = ('user', 'dateCreated', 'approved', 'active', 'dob')
        # error_messages = {"age": {"required": "Give yourself a username"}}
    def validate(self,data):
        print("App seria  ", data)
        # if not data['dob']:
        #     raise serializers.validation.ValidationError("Age must be above 18")
        
        # if data['age'] < 1:
        #     raise serializers.ValidationError("Age must be above 1")
        return data