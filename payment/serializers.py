from .models import Payment
from rest_framework import  serializers
from application.serializers import ApplicationSerializer
from user.serializers import UserSerializer
from insurance.serializers import InsuranceSerializer

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        optional_fields = ['dateCreated']
        fields = ('insurance','payment')
        
    def validate(self,data):
        if data['payment'] < 0:
            raise serializers.ValidationError("Premium must be 0 or greater")
        return data
  