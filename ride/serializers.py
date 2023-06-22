from rest_framework import serializers
from ride.models import*
from Userform.models import*


# class UserSerializerForm(serializers.Serializer):
#         pick_point=serializers.CharField(max_length=256)
#         drop_point=serializers.CharField(max_length=256)
        
        
        # def create(self, validated_data):
        #   return Bike_Trip(**validated_data)

class UserSerializerForm(serializers.ModelSerializer):
    class Meta:
        model = PICKFORM
        fields=['pick_point' , 'drop_point' ]
        # extra_kwargs = {'password': {'write_only': True}}
    
        def create(self, validated_data):
          return PICKFORM(**validated_data)


