from Userform.models import*
from rest_framework import serializers
from django.shortcuts import render ,HttpResponse, redirect
from ride.models import*
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import*
from rest_framework.response import Response
from rest_framework import response
import datetime
from rest_framework.serializers import*
from ride.serializers import*
from django.views import View
from ride.forms import*
import geopy
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
from geopy import*
from ride.pricechange import*
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import exceptions
from rest_framework.exceptions import APIException
from rest_framework.generics import GenericAPIView   
from rest_framework.views import APIView    
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
# UserSerializer
from rest_framework.permissions  import AllowAny
from rest_framework.reverse import reverse , reverse_lazy
from geopy.exc import GeocoderTimedOut

from Confirm_Booking.models import*

class RegisterAPI(ModelViewSet):
    serializer_class = UserSerializerForm
    permission_classes = [AllowAny]
    def get_queryset(self):
            post_data=PICKFORM.objects.all()
            return post_data


    def create(self, request, *args ,**Kwargs):
        serializer =self.get_serializer(data=request.data)
        # if serializer.is_valid():
        user=serializer.is_valid(raise_exception=True)
        # pick=serializer.validated_data.get('pick_point')
        # drop=serializer.validated_data.get('drop_point')
            # pick='delhi'
            # drop='ghaziabad'
            # pick_id=serializer.validated_data.get('id')
            # print(pick_id ,"ID Pick")
            # print(pick , "kasim saifi Pick")
            # print(drop , "kasim saifi Drop")
        
        pick=serializer.validated_data['pick_point']
        drop=serializer.validated_data['drop_point']
        print(pick , drop ,"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")  
        geolocator = Nominatim(user_agent="ride",timeout=10)
        location1 = geolocator.geocode(pick) 
        location2 = geolocator.geocode(drop)
            # print(location1 , "LOCATIONS1")
            # print(location2 , "LOCATIONS2")
        u1=pick=location1 
        u2=drop=location2 
        user1=PICKFORM.objects.all()
        for vehicle in Vehicle_type.objects.all():
                print(vehicle ,"Vehicle")
        for blero in Blero_8FT_Trip.objects.all():
                print(blero.extra2_distance ,"BLERO")
        for tata_8ft in Tata_ace_8FT_Trip.objects.all():
                print(tata_8ft.extra2_distance ,"TATA 8FT")
        for tata_7ft in Tata_ace_7FT_Trip.objects.all():
                print(tata_7ft.extra2_distance ,"TATA 7FT")
        for maruti in Maruti_suzuki_super_carry_Trip.objects.all():
                print(maruti.extra2_distance ,"MARUTI")
        for ecovan in Ecovan_Trip.objects.all():
                print(ecovan.extra2_distance ,"ECOVAN")
        for bike in Bike_Trip.objects.all():
                print(bike.extra2_distance ,"BIKE")
        for champion in Champion_Trip.objects.all():
                print(champion.extra2_distance ,"CHAMPION")
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        # dis=50.00    
        if u1 and u2:
                l1,l2=u1.latitude, u1.longitude
                l3,l4=u2.latitude, u2.longitude
                k = (l1, l2)
                de= (l3, l4)
                dis=great_circle(k, de).km
                # print(dis, "DISTANCE")
                user=request.user
                if location1 != None and location2 != None:
                    if current_time > '05:00:00' and current_time < '14:59:59':
                        if ( bike.extra1_distance >= dis or bike.extra2_distance >=dis 
                            or  champion.extra1_distance >= dis or champion.extra2_distance >= dis 
                            or ecovan.extra1_distance >= dis or ecovan.extra2_distance >= dis 
                            or  maruti.extra1_distance >= dis or maruti.extra2_distance >= dis
                            or  tata_7ft.extra1_distance >= dis or tata_7ft.extra2_distance >= dis
                            or  tata_8ft.extra1_distance >= dis or tata_8ft.extra2_distance >= dis
                            or  blero.extra1_distance >= dis or blero.extra2_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                             
                        elif ( bike.extra2_distance >= dis or bike.extra3_distance >=dis 
                            or  champion.extra2_distance >= dis or champion.extra3_distance >= dis 
                            or ecovan.extra2_distance >= dis or ecovan.extra3_distance >= dis 
                            or  maruti.extra2_distance >= dis or maruti.extra3_distance >= dis
                            or  tata_7ft.extra3_distance >= dis or tata_7ft.extra3_distance >= dis
                            or  tata_8ft.extra2_distance >= dis or tata_8ft.extra3_distance >= dis
                            or  blero.extra2_distance >= dis or blero.extra3_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                        
                        elif ( bike.extra3_distance >= dis or bike.extra4_distance >=dis 
                            or  champion.extra3_distance >= dis or champion.extra4_distance >= dis 
                            or ecovan.extra3_distance >= dis or ecovan.extra4_distance >= dis 
                            or  maruti.extra3_distance >= dis or maruti.extra4_distance >= dis
                            or  tata_7ft.extra3_distance >= dis or tata_7ft.extra4_distance >= dis
                            or  tata_8ft.extra3_distance >= dis or tata_8ft.extra4_distance >= dis
                            or  blero.extra3_distance >= dis or blero.extra4_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                        
                        elif ( bike.extra4_distance >= dis or bike.extra5_distance >=dis 
                            or  champion.extra4_distance >= dis or champion.extra5_distance >= dis 
                            or ecovan.extra4_distance >= dis or ecovan.extra5_distance >= dis 
                            or  maruti.extra4_distance >= dis or maruti.extra5_distance >= dis
                            or  tata_7ft.extra4_distance >= dis or tata_7ft.extra5_distance >= dis
                            or  tata_8ft.extra4_distance >= dis or tata_8ft.extra5_distance >= dis
                            or  blero.extra4_distance >= dis or blero.extra5_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                        
                        elif ( bike.extra5_distance >= dis or bike.extra6_distance >=dis 
                            or  champion.extra5_distance >= dis or champion.extra6_distance >= dis 
                            or ecovan.extra5_distance >= dis or ecovan.extra6_distance >= dis 
                            or  maruti.extra5_distance >= dis or maruti.extra6_distance >= dis
                            or  tata_7ft.extra5_distance >= dis or tata_7ft.extra6_distance >= dis
                            or  tata_8ft.extra5_distance >= dis or tata_8ft.extra6_distance >= dis
                            or  blero.extra5_distance >= dis or blero.extra6_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")

                        
                        elif ( bike.extra6_distance >= dis or dis 
                            or  champion.extra6_distance >= dis or  dis 
                            or ecovan.extra6_distance >= dis or dis 
                            or  maruti.extra6_distance >= dis or  dis
                            or  tata_7ft.extra6_distance >= dis or dis
                            or  tata_8ft.extra6_distance >= dis or dis
                            or  blero.extra6_distance >= dis or  dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                    elif current_time > '15:00:00' and current_time < '20:59:59':    
                        if ( bike.extra1_distance >= dis or bike.extra2_distance >=dis 
                            or  champion.extra1_distance >= dis or champion.extra2_distance >= dis 
                            or ecovan.extra1_distance >= dis or ecovan.extra2_distance >= dis 
                            or  maruti.extra1_distance >= dis or maruti.extra2_distance >= dis
                            or  tata_7ft.extra1_distance >= dis or tata_7ft.extra2_distance >= dis
                            or  tata_8ft.extra1_distance >= dis or tata_8ft.extra2_distance >= dis
                            or  blero.extra1_distance >= dis or blero.extra2_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                             
                        elif ( bike.extra2_distance >= dis or bike.extra3_distance >=dis 
                            or  champion.extra2_distance >= dis or champion.extra3_distance >= dis 
                            or ecovan.extra2_distance >= dis or ecovan.extra3_distance >= dis 
                            or  maruti.extra2_distance >= dis or maruti.extra3_distance >= dis
                            or  tata_7ft.extra3_distance >= dis or tata_7ft.extra3_distance >= dis
                            or  tata_8ft.extra2_distance >= dis or tata_8ft.extra3_distance >= dis
                            or  blero.extra2_distance >= dis or blero.extra3_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                        
                        elif ( bike.extra3_distance >= dis or bike.extra4_distance >=dis 
                            or  champion.extra3_distance >= dis or champion.extra4_distance >= dis 
                            or ecovan.extra3_distance >= dis or ecovan.extra4_distance >= dis 
                            or  maruti.extra3_distance >= dis or maruti.extra4_distance >= dis
                            or  tata_7ft.extra3_distance >= dis or tata_7ft.extra4_distance >= dis
                            or  tata_8ft.extra3_distance >= dis or tata_8ft.extra4_distance >= dis
                            or  blero.extra3_distance >= dis or blero.extra4_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                        
                        elif ( bike.extra4_distance >= dis or bike.extra5_distance >=dis 
                            or  champion.extra4_distance >= dis or champion.extra5_distance >= dis 
                            or ecovan.extra4_distance >= dis or ecovan.extra5_distance >= dis 
                            or  maruti.extra4_distance >= dis or maruti.extra5_distance >= dis
                            or  tata_7ft.extra4_distance >= dis or tata_7ft.extra5_distance >= dis
                            or  tata_8ft.extra4_distance >= dis or tata_8ft.extra5_distance >= dis
                            or  blero.extra4_distance >= dis or blero.extra5_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                        
                        elif ( bike.extra5_distance >= dis or bike.extra6_distance >=dis 
                            or  champion.extra5_distance >= dis or champion.extra6_distance >= dis 
                            or ecovan.extra5_distance >= dis or ecovan.extra6_distance >= dis 
                            or  maruti.extra5_distance >= dis or maruti.extra6_distance >= dis
                            or  tata_7ft.extra5_distance >= dis or tata_7ft.extra6_distance >= dis
                            or  tata_8ft.extra5_distance >= dis or tata_8ft.extra6_distance >= dis
                            or  blero.extra5_distance >= dis or blero.extra6_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")

                        
                        elif ( bike.extra6_distance >= dis or dis 
                            or  champion.extra6_distance >= dis or  dis 
                            or ecovan.extra6_distance >= dis or dis 
                            or  maruti.extra6_distance >= dis or  dis
                            or  tata_7ft.extra6_distance >= dis or dis
                            or  tata_8ft.extra6_distance >= dis or dis
                            or  blero.extra6_distance >= dis or  dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                    elif current_time > '21:00:00' and current_time < '04:59:59':
                        if ( bike.extra1_distance >= dis or bike.extra2_distance >=dis 
                            or  champion.extra1_distance >= dis or champion.extra2_distance >= dis 
                            or ecovan.extra1_distance >= dis or ecovan.extra2_distance >= dis 
                            or  maruti.extra1_distance >= dis or maruti.extra2_distance >= dis
                            or  tata_7ft.extra1_distance >= dis or tata_7ft.extra2_distance >= dis
                            or  tata_8ft.extra1_distance >= dis or tata_8ft.extra2_distance >= dis
                            or  blero.extra1_distance >= dis or blero.extra2_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                             
                        elif ( bike.extra2_distance >= dis or bike.extra3_distance >=dis 
                            or  champion.extra2_distance >= dis or champion.extra3_distance >= dis 
                            or ecovan.extra2_distance >= dis or ecovan.extra3_distance >= dis 
                            or  maruti.extra2_distance >= dis or maruti.extra3_distance >= dis
                            or  tata_7ft.extra3_distance >= dis or tata_7ft.extra3_distance >= dis
                            or  tata_8ft.extra2_distance >= dis or tata_8ft.extra3_distance >= dis
                            or  blero.extra2_distance >= dis or blero.extra3_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                        
                        elif ( bike.extra3_distance >= dis or bike.extra4_distance >=dis 
                            or  champion.extra3_distance >= dis or champion.extra4_distance >= dis 
                            or ecovan.extra3_distance >= dis or ecovan.extra4_distance >= dis 
                            or  maruti.extra3_distance >= dis or maruti.extra4_distance >= dis
                            or  tata_7ft.extra3_distance >= dis or tata_7ft.extra4_distance >= dis
                            or  tata_8ft.extra3_distance >= dis or tata_8ft.extra4_distance >= dis
                            or  blero.extra3_distance >= dis or blero.extra4_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                        
                        elif ( bike.extra4_distance >= dis or bike.extra5_distance >=dis 
                            or  champion.extra4_distance >= dis or champion.extra5_distance >= dis 
                            or ecovan.extra4_distance >= dis or ecovan.extra5_distance >= dis 
                            or  maruti.extra4_distance >= dis or maruti.extra5_distance >= dis
                            or  tata_7ft.extra4_distance >= dis or tata_7ft.extra5_distance >= dis
                            or  tata_8ft.extra4_distance >= dis or tata_8ft.extra5_distance >= dis
                            or  blero.extra4_distance >= dis or blero.extra5_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                            
                        
                        elif ( bike.extra5_distance >= dis or bike.extra6_distance >=dis 
                            or  champion.extra5_distance >= dis or champion.extra6_distance >= dis 
                            or ecovan.extra5_distance >= dis or ecovan.extra6_distance >= dis 
                            or  maruti.extra5_distance >= dis or maruti.extra6_distance >= dis
                            or  tata_7ft.extra5_distance >= dis or tata_7ft.extra6_distance >= dis
                            or  tata_8ft.extra5_distance >= dis or tata_8ft.extra6_distance >= dis
                            or  blero.extra5_distance >= dis or blero.extra6_distance >= dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")

                        
                        elif ( bike.extra6_distance >= dis or dis 
                            or  champion.extra6_distance >= dis or  dis 
                            or ecovan.extra6_distance >= dis or dis 
                            or  maruti.extra6_distance >= dis or  dis
                            or  tata_7ft.extra6_distance >= dis or dis
                            or  tata_8ft.extra6_distance >= dis or dis
                            or  blero.extra6_distance >= dis or  dis ):
                            
                            x=PICKFORM(
                                pick_point=location1,
                                drop_point=location2,
                                distance=dis,
                                # user_vehicle=user,
                                
                                )
                            x.save()
                            return HttpResponseRedirect(redirect_to="/check/pick_and_drop_api/api_view")
                                      
        return Response("Wrong location")





class Check(APIView):
    def get(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()
            vehicle = Vehicle_type.objects.all()
            for vehicle in vehicle: 
                print(vehicle, "kasim saifi ")
                print(vehicle.id)
            c1=Vehicle_type.objects.get(pk=1)
            c2=Vehicle_type.objects.get(pk=2)
            c3=Vehicle_type.objects.get(pk=3)
            c4=Vehicle_type.objects.get(pk=4)
            c5=Vehicle_type.objects.get(pk=5)
            c6=Vehicle_type.objects.get(pk=6)
            c7=Vehicle_type.objects.get(pk=7)
            
            
            print(c1.id,c2.id,c3.id,c4.id,c5.id,c6.id,c7.id, 'kkkkkasims akmsaiokksmkjw')
          
            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
                
           
            for blero in Blero_8FT_Trip.objects.all():
                print(blero.extra2_distance ,"BLERO")
                
            for tata_8ft in Tata_ace_8FT_Trip.objects.all():
                print(tata_8ft.extra2_distance ,"TATA 8FT")
                
            for tata_7ft in Tata_ace_7FT_Trip.objects.all():
                print(tata_7ft.extra2_distance ,"TATA 7FT")
                
            for maruti in Maruti_suzuki_super_carry_Trip.objects.all():
                print(maruti.extra2_distance ,"MARUTI")
                
            for ecovan in Ecovan_Trip.objects.all():
                print(ecovan.extra2_distance ,"ECOVAN")
                
            for bike in Bike_Trip.objects.all():
                print(bike.extra2_distance ,"BIKE")
                
            for champion in Champion_Trip.objects.all():
                print(champion.id ,"CHAMPION")
            
            for confirm in  Confirm_Booking.objects.all():
                print(confirm.id , "CONFIRM")
            
            fare1=bike.basefare+(PICK_FROM.distance - bike.basekm)*bike.price1_per_km
            fare2=champion.basefare+(PICK_FROM.distance - champion.basekm)*champion.price1_per_km
            fare3=ecovan.basefare+(PICK_FROM.distance - ecovan.basekm)*ecovan.price1_per_km
            fare4=maruti.basefare+(PICK_FROM.distance - maruti.basekm)*maruti.price1_per_km
            fare5=tata_7ft.basefare+(PICK_FROM.distance - tata_7ft.basekm)*tata_7ft.price1_per_km
            fare6=tata_8ft.basefare+(PICK_FROM.distance - tata_8ft.basekm)*tata_8ft.price1_per_km
            fare7=blero.basefare+(PICK_FROM.distance - blero.basekm)*blero.price1_per_km
            context={
                'fare1':fare1,
                'fare2':fare2,
                'fare3':fare3,
                'fare4':fare4,
                'fare5':fare5,
                'fare6':fare6,
                'fare7':fare7,
                'data':all_data,
                'vehicle':vehicle,
                'c1':c1,
                'c2':c2,
                'c3':c3,
                'c4':c4,
                'c5':c5,
                'c6':c6,
                'c7':c7,
                
            }
            return render(request , 'other.html',context)


class Check_bike(APIView):
    def get(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()
            c1=Vehicle_type.objects.get(pk=1)
            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for bike in Bike_Trip.objects.all():
                print(bike.id ,"CHAMPION")
            fare1=bike.basefare+(PICK_FROM.distance - bike.basekm)*bike.price1_per_km
            context={
                'fare1':fare1,
                'data':all_data,
                'c1':c1,
            }
            return render(request , 'bike.html',context)
        
    def post(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()
            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for bike in Bike_Trip.objects.all():
                print(bike.extra2_distance ,"CHAMPION")
            
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            c1=Vehicle_type.objects.get(pk=1)
            if request.user.is_anonymous==True:
                return HttpResponse("Please Login  <a href='/check/pick_and_drop_api/api_view'>BACK </a>")
            if  c1:
                fare1=bike.basefare+(PICK_FROM.distance - bike.basekm)*bike.price2_per_km
                x=Confirm_Booking(
                user=request.user,
                pick_point=PICK_FROM.pick_point,
                drop_point=PICK_FROM.drop_point,
                price=fare1,
                distance=PICK_FROM.distance,
                vehicle=c1,
                )
                x.save()
            return redirect("/success")


class Check_Champion(APIView):
    def get(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()
            c2=Vehicle_type.objects.get(pk=2)
            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for champion in Champion_Trip.objects.all():
                print(champion.id ,"CHAMPION")
            fare2=champion.basefare+(PICK_FROM.distance - champion.basekm)*champion.price1_per_km
            context={
                'fare2':fare2,
                'data':all_data,
                'c2':c2,
            }
            return render(request , 'champion.html',context)
        
    def post(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()

            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for champion in Champion_Trip.objects.all():
                print(champion.extra2_distance ,"CHAMPION")
            
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            c2=Vehicle_type.objects.get(pk=2)
            if request.user.is_anonymous==True:
                return HttpResponse("Please Login  <a href='/check/pick_and_drop_api/api_view'>BACK </a>")
            if  c2:
                fare2=champion.basefare+(PICK_FROM.distance - champion.basekm)*champion.price2_per_km
                x=Confirm_Booking(
                user=request.user,
                pick_point=PICK_FROM.pick_point,
                drop_point=PICK_FROM.drop_point,
                price=fare2,
                distance=PICK_FROM.distance,
                vehicle=c2,
                )
                x.save()
            return redirect("/success")



class Check_ecovan(APIView):
    def get(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()
            c3=Vehicle_type.objects.get(pk=3)
            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for ecovan in Ecovan_Trip.objects.all():
                print(ecovan.id ,"CHAMPION")
            fare3=ecovan.basefare+(PICK_FROM.distance - ecovan.basekm)*ecovan.price1_per_km
            context={
                'fare3':fare3,
                'data':all_data,
                'c3':c3,
            }
            return render(request , 'ecovan.html',context)
        
    def post(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()

            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for ecovan in Ecovan_Trip.objects.all():
                print(ecovan.extra2_distance ,"CHAMPION")
            
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            c3=Vehicle_type.objects.get(pk=3)
            if request.user.is_anonymous==True:
                return HttpResponse("Please Login  <a href='/check/pick_and_drop_api/api_view'>BACK </a>")
            if  c3:
                fare3=ecovan.basefare+(PICK_FROM.distance - ecovan.basekm)*ecovan.price2_per_km
                x=Confirm_Booking(
                user=request.user,
                pick_point=PICK_FROM.pick_point,
                drop_point=PICK_FROM.drop_point,
                price=fare3,
                distance=PICK_FROM.distance,
                vehicle=c3,
                )
                x.save()
            return redirect("/success")


class Check_Maruti_suzuki_super_carry_Trip(APIView):
    def get(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()
            c4=Vehicle_type.objects.get(pk=4)
            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for maruti in Maruti_suzuki_super_carry_Trip.objects.all():
                print(maruti.id ,"")
            fare4=maruti.basefare+(PICK_FROM.distance - maruti.basekm)*maruti.price1_per_km
            context={
                'fare4':fare4,
                'data':all_data,
                'c4':c4,
            }
            return render(request , 'maruti.html',context)
        
    def post(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()

            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for maruti in Maruti_suzuki_super_carry_Trip.objects.all():
                print(maruti.extra2_distance ,"")
            
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            c4=Vehicle_type.objects.get(pk=4)
            if request.user.is_anonymous==True:
                return HttpResponse("Please Login  <a href='/check/pick_and_drop_api/api_view'>BACK </a>")
            if  c4:
                fare4=maruti.basefare+(PICK_FROM.distance - maruti.basekm)*maruti.price2_per_km
                x=Confirm_Booking(
                user=request.user,
                pick_point=PICK_FROM.pick_point,
                drop_point=PICK_FROM.drop_point,
                price=fare4,
                distance=PICK_FROM.distance,
                vehicle=c4,
                )
                x.save()
            return redirect("/success")


class Check_Tata_ace_7FT_Trip(APIView):
    def get(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()
            c5=Vehicle_type.objects.get(pk=5)
            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for tata_7ft in Tata_ace_7FT_Trip.objects.all():
                print(tata_7ft.id ,"")
            fare5=tata_7ft.basefare+(PICK_FROM.distance - tata_7ft.basekm)*tata_7ft.price1_per_km
            context={
                'fare5':fare5,
                'data':all_data,
                'c5':c5,
            }
            return render(request , 'tata_7ft.html',context)
        
    def post(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()

            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for tata_7ft in Tata_ace_7FT_Trip.objects.all():
                print(tata_7ft.extra2_distance ,"")
            
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            c5=Vehicle_type.objects.get(pk=5)
            if request.user.is_anonymous==True:
                return HttpResponse("Please Login  <a href='/check/pick_and_drop_api/api_view'>BACK </a>") 
            if  c5:
                fare5=tata_7ft.basefare+(PICK_FROM.distance - tata_7ft.basekm)*tata_7ft.price2_per_km
                x=Confirm_Booking(
                user=request.user,
                pick_point=PICK_FROM.pick_point,
                drop_point=PICK_FROM.drop_point,
                price=fare5,
                distance=PICK_FROM.distance,
                vehicle=c5,
                )
                x.save()
            return redirect("/success")


class Check_Tata_ace_8FT_Trip(APIView):
    def get(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()
            c6=Vehicle_type.objects.get(pk=6)
            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for tata_8ft in Tata_ace_8FT_Trip.objects.all():
                print(tata_8ft.id ,"")
            fare6=tata_8ft.basefare+(PICK_FROM.distance - tata_8ft.basekm)*tata_8ft.price1_per_km
            context={
                'fare6':fare6,
                'data':all_data,
                'c6':c6,
            }
            return render(request , 'tata_8ft.html',context)
        
    def post(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()

            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for tata_8ft in Tata_ace_8FT_Trip.objects.all():
                print(tata_8ft.extra2_distance ,"")
            
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            c6=Vehicle_type.objects.get(pk=6)
            if request.user.is_anonymous==True:
                return HttpResponse("Please Login  <a href='/check/pick_and_drop_api/api_view'>BACK </a>")
            if  c6:
                fare6=tata_8ft.basefare+(PICK_FROM.distance - tata_8ft.basekm)*tata_8ft.price2_per_km
                x=Confirm_Booking(
                user=request.user,
                pick_point=PICK_FROM.pick_point,
                drop_point=PICK_FROM.drop_point,
                price=fare6,
                distance=PICK_FROM.distance,
                vehicle=c6,
                )
                x.save()
            return redirect("/success")


class Check_Blero_8FT_Trip(APIView):
    def get(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()
            c7=Vehicle_type.objects.get(pk=7)
            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for blero in Blero_8FT_Trip.objects.all():
                print(blero.id ,"CHAMPION")
            fare7=blero.basefare+(PICK_FROM.distance - blero.basekm)*blero.price1_per_km
            context={
                'fare7':fare7,
                'data':all_data,
                'c7':c7,
            }
            return render(request , 'blero.html',context)
        
    def post(self ,request , format=None):
            all_data=PICKFORM.objects.all().last()

            for PICK_FROM in PICKFORM.objects.all():
                print(PICK_FROM,"PICKFORM")
            for blero in Blero_8FT_Trip.objects.all():
                print(blero.extra2_distance ,"CHAMPION")
            
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            c7=Vehicle_type.objects.get(pk=7)
            if request.user.is_anonymous==True:
                return HttpResponse("Please Login  <a href='/check/pick_and_drop_api/api_view'>BACK </a>") 
            if  c7:
                fare7=blero.basefare+(PICK_FROM.distance - blero.basekm)*blero.price2_per_km
                x=Confirm_Booking(
                user=request.user,
                pick_point=PICK_FROM.pick_point,
                drop_point=PICK_FROM.drop_point,
                price=fare7,
                distance=PICK_FROM.distance,
                vehicle=c7,
                )
                x.save()
            return redirect("/success")

def success(request):
    return render(request , 'success.html')           
                        
                                
            









