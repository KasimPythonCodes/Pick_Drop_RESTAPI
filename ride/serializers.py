from rest_framework import serializers
from ride.models import*

# class Testrider(serializers.ModelSerializer):
#     # id=serializers.PrimaryKeyRelatedField(many=True ,read_only=True)
#     class Meta:
#         model=User_pick_form
#         fields=['select_truck_type' ,'pick_point' , 'drop_point' ]


# class TestKasim(serializers.ModelSerializer):
#     class Meta:
#         model=Rider_Trip
#         fields=['basefare' ,'basekm' , 'distance','price_per_km','total_price' ]        



class UserSerializerForm(serializers.ModelSerializer):
    class Meta:
        model = User_pick_form
        fields=['select_truck_type' ,'pick_point' , 'drop_point' ]
        # extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user =User_pick_form.objects.create(select_truck_type=validated_data['select_truck_type'],
        pick_point=validated_data['pick_point'], drop_point=validated_data['drop_point'])
        return user
