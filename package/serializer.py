from insurance.serializers import InsuranceSerializer
from .models import Package
from insurance.models import Insurance
from rest_framework import  serializers
from application.serializers import ApplicationSerializer
from user.serializers import UserSerializer





class PackageSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # user = serializers.RelatedField(read_only=True)
    # insurances = InsuranceSerializer()
    # application = ApplicationSerializer()
    # application = serializers.RelatedField(read_only=True)
    class Meta:
        model = Package
        optional_fields = []
        fields = ('insurances', 'soldFor', 'dateCreated', 'dateApproved', 'dateModified')

    
    def create(self, validated_data):
        package = Package(**validated_data)
        insurance = Insurance.objects.get(id=5)
        print("The insurance obj found ", insurance)
        package.insurances.add(insurance)
        package.save()
    
    def validate(self,data):    
        if data['premium'] < 0:
            raise serializers.ValidationError("Premium must be 0 or greater")
        return data
