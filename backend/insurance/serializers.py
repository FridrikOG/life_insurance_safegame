from .models import Insurance
from rest_framework import  serializers
from application.serializers import ApplicationSerializer
from user.serializers import UserSerializer

class InsuranceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # user = serializers.RelatedField(read_only=True)
    #  team = serializers.RelatedField()
    application = ApplicationSerializer()
    # application = serializers.RelatedField(read_only=True)
    class Meta:
        model = Insurance
        optional_fields = ['user_id','dateCreated', 'dateApproved', 'dateExpires']
        fields = ('user_id', 'user','application', 'premium', 'application', 'dateCreated','dateApproved', 'dateExpires')
    
    def create(self, validated_data):
        insurance = Insurance(**validated_data)
        insurance.save()
    
    def validate(self,data):    
        if data['premium'] < 0:
            raise serializers.ValidationError("Premium must be 0 or greater")
        return data
